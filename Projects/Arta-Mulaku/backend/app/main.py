from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Simple Chat CRUD API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def serialize_conversation(conversation: models.Conversation) -> schemas.ConversationRead:
    return schemas.ConversationRead(
        id=conversation.id,
        title=conversation.title,
        created_at=conversation.created_at,
        participants=[
            schemas.ParticipantRead(id=member.user.id, name=member.user.name)
            for member in conversation.participants
        ],
    )


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/users", response_model=list[schemas.UserRead])
def get_users(db: Session = Depends(get_db)):
    return crud.list_users(db)


@app.post("/users", response_model=schemas.UserRead, status_code=status.HTTP_201_CREATED)
def create_user(payload: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_user(db, payload)
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User name must be unique.",
        ) from exc


@app.put("/users/{user_id}", response_model=schemas.UserRead)
def update_user(user_id: int, payload: schemas.UserUpdate, db: Session = Depends(get_db)):
    try:
        user = crud.update_user(db, user_id, payload)
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User name must be unique.",
        ) from exc
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    return user


@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    if not crud.delete_user(db, user_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")


@app.get("/conversations", response_model=list[schemas.ConversationRead])
def get_conversations(db: Session = Depends(get_db)):
    return [serialize_conversation(item) for item in crud.list_conversations(db)]


@app.post(
    "/conversations",
    response_model=schemas.ConversationRead,
    status_code=status.HTTP_201_CREATED,
)
def create_conversation(
    payload: schemas.ConversationCreate, db: Session = Depends(get_db)
):
    conversation = crud.create_conversation(db, payload)
    if conversation is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Participants must exist and be unique.",
        )
    return serialize_conversation(conversation)


@app.put("/conversations/{conversation_id}", response_model=schemas.ConversationRead)
def update_conversation(
    conversation_id: int,
    payload: schemas.ConversationUpdate,
    db: Session = Depends(get_db),
):
    conversation = crud.update_conversation(db, conversation_id, payload)
    if conversation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conversation not found or participants invalid.",
        )
    return serialize_conversation(conversation)


@app.delete("/conversations/{conversation_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_conversation(conversation_id: int, db: Session = Depends(get_db)):
    if not crud.delete_conversation(db, conversation_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conversation not found.",
        )


@app.get(
    "/conversations/{conversation_id}/messages",
    response_model=list[schemas.MessageRead],
)
def get_messages(conversation_id: int, db: Session = Depends(get_db)):
    conversation = crud.get_conversation(db, conversation_id)
    if conversation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conversation not found.",
        )
    return crud.list_messages(db, conversation_id)


@app.post(
    "/conversations/{conversation_id}/messages",
    response_model=schemas.MessageRead,
    status_code=status.HTTP_201_CREATED,
)
def create_message(
    conversation_id: int,
    payload: schemas.MessageCreate,
    db: Session = Depends(get_db),
):
    message = crud.create_message(db, conversation_id, payload)
    if message is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Conversation or sender is invalid.",
        )
    return message


@app.put("/messages/{message_id}", response_model=schemas.MessageRead)
def update_message(
    message_id: int, payload: schemas.MessageUpdate, db: Session = Depends(get_db)
):
    message = crud.update_message(db, message_id, payload)
    if message is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Message not found.",
        )
    return message


@app.delete("/messages/{message_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_message(message_id: int, db: Session = Depends(get_db)):
    if not crud.delete_message(db, message_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Message not found.",
        )
