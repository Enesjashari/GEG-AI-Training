import os
import re
import json
import hashlib
from pathlib import Path
from typing import List, Dict, Tuple, Any

import numpy as np
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader


# =========================
# Configuration
# =========================
PDF_PATH = r"C:\Users\Admin\Desktop\GEG-AI-Training\M4 - L1\senior_software_developer_resume.pdf"

CHAT_MODEL = "gpt-4o-mini"
EMBEDDING_MODEL = "text-embedding-3-small"

MAX_CHUNK_CHARS = 900
TOP_K = 5

MIN_RELEVANCE_SCORE_QA = 0.18
MIN_RELEVANCE_SCORE_GENERATION = 0.10

CACHE_DIR = Path("./cache")
CACHE_DIR.mkdir(exist_ok=True)


# =========================
# OpenAI Client
# =========================
def load_api_client() -> OpenAI:
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY was not found in your .env file")

    return OpenAI(api_key=api_key)


# =========================
# PDF Extraction
# =========================
def extract_pdf_pages(pdf_path: str) -> List[Dict[str, Any]]:
    reader = PdfReader(pdf_path)
    pages = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        text = text.strip()

        if text:
            pages.append({
                "page_number": i + 1,
                "text": text
            })

    if not pages:
        raise ValueError("No text could be extracted from the PDF.")

    return pages


# =========================
# Text Helpers
# =========================
def normalize_text(text: str) -> str:
    text = re.sub(r"\r", "\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def split_into_paragraphs(text: str) -> List[str]:
    text = normalize_text(text)
    return [p.strip() for p in text.split("\n\n") if p.strip()]


SECTION_HEADERS = {
    "professional experience",
    "technical skills",
    "skills",
    "education",
    "certifications",
    "achievements",
    "projects",
    "summary",
    "contact",
    "languages",
}


def detect_section_title(paragraph: str) -> bool:
    stripped = paragraph.strip().lower()
    return stripped in SECTION_HEADERS


def tokenize(text: str) -> List[str]:
    return re.findall(r"[a-zA-Z0-9@.+_-]+", text.lower())


# =========================
# Chunking
# =========================
def build_chunks(pages: List[Dict[str, Any]], max_chunk_chars: int = 900) -> List[Dict[str, Any]]:
    chunks = []

    for page in pages:
        page_number = page["page_number"]
        paragraphs = split_into_paragraphs(page["text"])

        current_chunk: List[str] = []
        current_len = 0
        current_section = "General"

        for para in paragraphs:
            if detect_section_title(para):
                if current_chunk:
                    chunks.append({
                        "page_number": page_number,
                        "section": current_section,
                        "text": "\n\n".join(current_chunk).strip()
                    })
                    current_chunk = []
                    current_len = 0
                current_section = para.strip()
                current_chunk.append(para)
                current_len += len(para)
                continue

            para_len = len(para)

            if current_len + para_len + 2 > max_chunk_chars and current_chunk:
                chunks.append({
                    "page_number": page_number,
                    "section": current_section,
                    "text": "\n\n".join(current_chunk).strip()
                })
                current_chunk = [para]
                current_len = para_len
            else:
                current_chunk.append(para)
                current_len += para_len + 2

        if current_chunk:
            chunks.append({
                "page_number": page_number,
                "section": current_section,
                "text": "\n\n".join(current_chunk).strip()
            })

    return chunks


# =========================
# Cache
# =========================
def file_hash(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def cache_paths(pdf_path: str, model_name: str) -> Tuple[Path, Path]:
    base = f"{file_hash(pdf_path)}_{model_name.replace('/', '_')}"
    return CACHE_DIR / f"{base}_chunks.json", CACHE_DIR / f"{base}_embeddings.npy"


def save_cache(chunks: List[Dict[str, Any]], embeddings: np.ndarray, chunks_path: Path, emb_path: Path) -> None:
    with open(chunks_path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)
    np.save(emb_path, embeddings)


def load_cache(chunks_path: Path, emb_path: Path) -> Tuple[List[Dict[str, Any]], np.ndarray]:
    with open(chunks_path, "r", encoding="utf-8") as f:
        chunks = json.load(f)
    embeddings = np.load(emb_path)
    return chunks, embeddings


# =========================
# Embeddings
# =========================
def get_embeddings(client: OpenAI, texts: List[str]) -> np.ndarray:
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=texts
    )
    return np.array([item.embedding for item in response.data], dtype=np.float32)


def cosine_similarity_matrix(query_vec: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    query_norm = np.linalg.norm(query_vec)
    matrix_norms = np.linalg.norm(matrix, axis=1)

    denom = matrix_norms * query_norm
    denom[denom == 0] = 1e-9

    return np.dot(matrix, query_vec) / denom


# =========================
# Retrieval Helpers
# =========================
def keyword_overlap_score(question: str, chunk_text: str) -> float:
    q_tokens = set(tokenize(question))
    c_tokens = set(tokenize(chunk_text))

    if not q_tokens:
        return 0.0

    overlap = q_tokens.intersection(c_tokens)
    return len(overlap) / len(q_tokens)


def is_contact_question(question: str) -> bool:
    q = question.lower()
    patterns = [
        "phone", "number", "contact", "email", "linkedin", "github",
        "website", "social media", "call you", "text you"
    ]
    return any(p in q for p in patterns)


def is_generation_request(question: str) -> bool:
    q = question.lower().strip()

    generation_patterns = [
        "about me",
        "write about me",
        "create about me",
        "make about me",
        "professional summary",
        "summary about me",
        "bio",
        "biography",
        "profile summary",
        "objective statement",
        "personal summary",
        "short intro",
        "introduction about me",
        "write a summary",
        "create a summary",
        "make a summary",
        "create me a summary",
        "create me about me",
        "write an about me",
        "create an about me",
    ]

    return any(pattern in q for pattern in generation_patterns)


def rewrite_query_for_retrieval(question: str) -> str:
    if is_generation_request(question):
        return (
            "professional summary experience skills achievements education "
            "latest role previous roles technical skills certifications"
        )
    return question


def extract_contact_info(full_text: str) -> Dict[str, List[str]]:
    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", full_text)
    linkedin = re.findall(r"(?:https?://)?(?:www\.)?linkedin\.com/[^\s•|]+", full_text, re.IGNORECASE)
    github = re.findall(r"(?:https?://)?(?:www\.)?github\.com/[^\s•|]+", full_text, re.IGNORECASE)
    websites = re.findall(r"(?:https?://)?(?:www\.)?[A-Za-z0-9-]+\.[A-Za-z]{2,}(?:/[^\s•|]+)?", full_text)
    phones = re.findall(r"(?:\+?\d[\d\s().-]{6,}\d)", full_text)

    return {
        "emails": sorted(set(emails)),
        "linkedin": sorted(set(linkedin)),
        "github": sorted(set(github)),
        "phones": sorted(set(phones)),
        "websites": sorted(set(websites)),
    }


def retrieve_relevant_chunks(
    client: OpenAI,
    question: str,
    chunks: List[Dict[str, Any]],
    chunk_embeddings: np.ndarray,
    top_k: int = TOP_K
) -> List[Dict[str, Any]]:
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=[question]
    )
    query_vec = np.array(response.data[0].embedding, dtype=np.float32)

    semantic_scores = cosine_similarity_matrix(query_vec, chunk_embeddings)

    scored = []
    for idx, chunk in enumerate(chunks):
        semantic = float(semantic_scores[idx])
        keyword = keyword_overlap_score(question, chunk["text"])
        final_score = (0.80 * semantic) + (0.20 * keyword)

        scored.append({
            "chunk": chunk,
            "semantic_score": semantic,
            "keyword_score": keyword,
            "final_score": final_score
        })

    scored.sort(key=lambda x: x["final_score"], reverse=True)
    return scored[:top_k]


def build_context(relevant_chunks: List[Dict[str, Any]]) -> str:
    blocks = []
    for item in relevant_chunks:
        chunk = item["chunk"]
        blocks.append(
            f"[Page {chunk['page_number']} | Section: {chunk['section']} | Score: {item['final_score']:.3f}]\n"
            f"{chunk['text']}"
        )
    return "\n\n---\n\n".join(blocks)


# =========================
# Answering
# =========================
def answer_question(
    client: OpenAI,
    question: str,
    relevant_chunks: List[Dict[str, Any]],
    full_text: str
) -> str:
    q = question.lower().strip()

    if is_contact_question(q):
        contact = extract_contact_info(full_text)

        if "email" in q and contact["emails"]:
            return f"Yes. Email: {', '.join(contact['emails'])}"
        if "linkedin" in q and contact["linkedin"]:
            return f"Yes. LinkedIn: {', '.join(contact['linkedin'])}"
        if "github" in q and contact["github"]:
            return f"Yes. GitHub: {', '.join(contact['github'])}"
        if ("phone" in q or "number" in q or "call" in q) and contact["phones"]:
            return f"Yes. Phone: {', '.join(contact['phones'])}"
        if "website" in q and contact["websites"]:
            return f"Yes. Website: {', '.join(contact['websites'])}"
        if ("contact" in q or "social media" in q or "text you" in q):
            parts = []
            if contact["emails"]:
                parts.append(f"Email: {', '.join(contact['emails'])}")
            if contact["linkedin"]:
                parts.append(f"LinkedIn: {', '.join(contact['linkedin'])}")
            if contact["github"]:
                parts.append(f"GitHub: {', '.join(contact['github'])}")
            if contact["phones"]:
                parts.append(f"Phone: {', '.join(contact['phones'])}")
            if contact["websites"]:
                parts.append(f"Website: {', '.join(contact['websites'])}")

            if parts:
                return "Yes. " + " | ".join(parts)

        return "I could not find that in the provided PDF."

    if is_generation_request(q):
        if not relevant_chunks or relevant_chunks[0]["final_score"] < MIN_RELEVANCE_SCORE_GENERATION:
            return "I could not find enough information in the provided PDF to create that."

        context = build_context(relevant_chunks[:5])

        prompt = f"""
You are a professional resume assistant.

Your task is to write a polished professional summary using ONLY the facts from the PDF context.

Rules:
1. Use only information found in the context.
2. Do not invent companies, years, technologies, or achievements.
3. If the user asks for "about me", write a concise professional summary.
4. Default to third-person resume style unless the user clearly asks for first person.
5. Keep it between 80 and 140 words unless the user asks otherwise.
6. Do not mention page numbers in the final answer.
7. If there is not enough information, say exactly:
I could not find enough information in the provided PDF to create that.

PDF Context:
{context}

User Request:
{question}
""".strip()

        response = client.responses.create(
            model=CHAT_MODEL,
            input=prompt
        )

        answer = response.output_text.strip()
        return answer if answer else "I could not find enough information in the provided PDF to create that."

    if not relevant_chunks or relevant_chunks[0]["final_score"] < MIN_RELEVANCE_SCORE_QA:
        return "I could not find that in the provided PDF."

    context = build_context(relevant_chunks)

    prompt = f"""
You are a resume Q&A assistant.

You must answer ONLY from the provided PDF context.

Rules:
1. If the answer is clearly present in the context, answer concisely.
2. If the answer is not present, say exactly:
I could not find that in the provided PDF.
3. Do not invent missing facts.
4. If helpful, mention the page number(s) like: (Page 2)
5. Keep the tone professional and direct.
6. For work experience questions, summarize responsibilities clearly.

PDF Context:
{context}

User Question:
{question}
""".strip()

    response = client.responses.create(
        model=CHAT_MODEL,
        input=prompt
    )

    answer = response.output_text.strip()
    return answer if answer else "I could not find that in the provided PDF."


# =========================
# Index Preparation
# =========================
def prepare_index(client: OpenAI, pdf_path: str) -> Tuple[List[Dict[str, Any]], np.ndarray, str]:
    chunks_path, emb_path = cache_paths(pdf_path, EMBEDDING_MODEL)

    pages = extract_pdf_pages(pdf_path)
    full_text = "\n\n".join([f"[Page {p['page_number']}]\n{p['text']}" for p in pages])

    if chunks_path.exists() and emb_path.exists():
        chunks, embeddings = load_cache(chunks_path, emb_path)
        return chunks, embeddings, full_text

    chunks = build_chunks(pages, max_chunk_chars=MAX_CHUNK_CHARS)
    chunk_texts = [c["text"] for c in chunks]
    embeddings = get_embeddings(client, chunk_texts)

    save_cache(chunks, embeddings, chunks_path, emb_path)
    return chunks, embeddings, full_text


# =========================
# Debug
# =========================
def print_debug_results(relevant_chunks: List[Dict[str, Any]]) -> None:
    print("\n[DEBUG] Top retrieved chunks:")
    for i, item in enumerate(relevant_chunks, start=1):
        chunk = item["chunk"]
        preview = chunk["text"][:160].replace("\n", " ")
        print(
            f"{i}. Page {chunk['page_number']} | Section: {chunk['section']} | "
            f"Semantic: {item['semantic_score']:.3f} | "
            f"Keyword: {item['keyword_score']:.3f} | "
            f"Final: {item['final_score']:.3f}"
        )
        print(f"   Preview: {preview}...")
    print()


# =========================
# Main
# =========================
def main() -> None:
    try:
        print("Loading assistant...\n")
        client = load_api_client()

        print("Reading and indexing PDF...")
        chunks, chunk_embeddings, full_text = prepare_index(client, PDF_PATH)

        print("Assistant is ready.")
        print(f"Indexed {len(chunks)} chunks.")
        print("Type your question about the PDF.")
        print("Type 'exit' to quit.\n")

        while True:
            question = input("You: ").strip()

            if question.lower() in {"exit", "quit"}:
                print("Goodbye.")
                break

            if not question:
                continue

            search_query = rewrite_query_for_retrieval(question)

            relevant_chunks = retrieve_relevant_chunks(
                client=client,
                question=search_query,
                chunks=chunks,
                chunk_embeddings=chunk_embeddings,
                top_k=TOP_K
            )

            print_debug_results(relevant_chunks)

            answer = answer_question(
                client=client,
                question=question,
                relevant_chunks=relevant_chunks,
                full_text=full_text
            )

            print("Assistant:")
            print(answer)
            print()

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()