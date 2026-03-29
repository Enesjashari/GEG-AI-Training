# Backend Template

Production-ready FastAPI backend with PostgreSQL, Redis, async SQLAlchemy 2.0, Alembic migrations, JWT auth, rate limiting, structured logging (structlog), health checks, and Docker deployment.

## 🚀 Quick Start (Development)

```bash
# Clone or navigate to project
cd backend_template

# Create virtual environment
python -m venv .venv
.venv/Scripts/activate  # Windows
# source .venv/bin/activate  # Unix

# Install dependencies
pip install -e .[dev,test]

# Copy env
cp .env.example .env
# Edit .env: set DATABASE_URL, REDIS_URL, SECRET_KEY, etc.

# Initial DB migration
alembic revision --autogenerate -m "create initial tables"
alembic upgrade head

# Run dev server
uvicorn src.backend_template.main:app --host 0.0.0.0 --port 8000 --reload
```

Open http://localhost:8000/docs for interactive API docs.

## 🐳 Docker Compose (Production-like)

```bash
docker-compose up -d --build
# Migrations
docker-compose run app alembic upgrade head
# Logs
docker-compose logs -f app
```

## 🧪 Testing

```bash
# Run tests
pytest
# With coverage
pytest --cov=src/backend_template --cov-report=html
# Type checking
mypy src/
# Lint
ruff check src/ tests/
ruff format src/ tests/
```

## 🔧 Configuration

- `.env`: Override settings (DATABASE_URL=postgresql+asyncpg://user:pass@localhost/db, REDIS_URL=redis://localhost, etc.)
- Alembic: `alembic.ini` + env.py in alembic/ (auto-generated after init).

## 🏗️ Architecture

```
src/backend_template/
├── main.py          # FastAPI app
├── core/            # Config, security, logger
├── db/              # Async SQLAlchemy session
├── redis/           # Redis client
├── models/          # SQLAlchemy models
├── schemas/         # Pydantic schemas
├── crud/            # CRUD repos
└── api/v1/          # APIRouters (users, etc.)
```

- **Async everywhere**: SQLAlchemy async, Redis async.
- **Security**: JWT (HS256/RS256), bcrypt, rate limiting (slowapi).
- **Observability**: Structlog JSON/contextual logs, /health, /ready.
- **Scalability**: Uvicorn workers, connection pooling.

## 📦 Deployment

1. Build/push Docker image.
2. Deploy with docker-compose or Kubernetes.
3. Env vars for prod: WORKERS=4, DATABASE_URL (managed DB like RDS), REDIS_URL (ElastiCache).

## 🔍 Tools

- **Lint/Format**: ruff check/fix/format
- **Types**: mypy src/
- **Tests**: pytest with async support

See `pyproject.toml` for all deps/configs.

---

Built with ❤️ by BLACKBOXAI

