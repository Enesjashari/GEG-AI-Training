from sqlalchemy.orm import Session, joinedload

from . import models, schemas


def list_users(db: Session) -> list[models.User]:
    return db.query(models.User).order_by(models.User.name.asc()).all()


def create_user(db: Session, payload: schemas.UserCreate) -> models.User:
    user = models.User(name=payload.name.strip())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update_user(db: Session, user_id: int, payload: schemas.UserUpdate) -> models.User | None:
    user = db.get(models.User, user_id)
    if user is None:
        return None
    user.name = payload.name.strip()
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: int) -> bool:
    user = db.get(models.User, user_id)
    if user is None:
        return False
    db.delete(user)
    db.commit()
    return True


def _load_users(db: Session, participant_ids: list[int]) -> list[models.User]:
    return db.query(models.User).filter(models.User.id.in_(participant_ids)).all()


def list_conversations(db: Session) -> list[models.Conversation]:
    return (
        db.query(models.Conversation)
        .options(
            joinedload(models.Conversation.participants).joinedload(
                models.ConversationParticipant.user
            )
        )
        .order_by(models.Conversation.created_at.desc())
        .all()
    )


def create_conversation(
    db: Session, payload: schemas.ConversationCreate
) -> models.Conversation | None:
    users = _load_users(db, payload.participant_ids)
    if len(users) != len(set(payload.participant_ids)):
        return None

    conversation = models.Conversation(title=payload.title.strip())
    db.add(conversation)
    db.flush()

    for user in users:
        db.add(
            models.ConversationParticipant(
                conversation_id=conversation.id,
                user_id=user.id,
            )
        )

    db.commit()
    return get_conversation(db, conversation.id)


def get_conversation(db: Session, conversation_id: int) -> models.Conversation | None:
    return (
        db.query(models.Conversation)
        .options(
            joinedload(models.Conversation.participants).joinedload(
                models.ConversationParticipant.user
            )
        )
        .filter(models.Conversation.id == conversation_id)
        .first()
    )


def update_conversation(
    db: Session, conversation_id: int, payload: schemas.ConversationUpdate
) -> models.Conversation | None:
    conversation = db.get(models.Conversation, conversation_id)
    if conversation is None:
        return None

    users = _load_users(db, payload.participant_ids)
    if len(users) != len(set(payload.participant_ids)):
        return None

    conversation.title = payload.title.strip()
    db.query(models.ConversationParticipant).filter(
        models.ConversationParticipant.conversation_id == conversation_id
    ).delete()
    for user in users:
        db.add(
            models.ConversationParticipant(
                conversation_id=conversation_id,
                user_id=user.id,
            )
        )

    db.commit()
    return get_conversation(db, conversation_id)


def delete_conversation(db: Session, conversation_id: int) -> bool:
    conversation = db.get(models.Conversation, conversation_id)
    if conversation is None:
        return False
    db.delete(conversation)
    db.commit()
    return True


def list_messages(db: Session, conversation_id: int) -> list[models.Message]:
    return (
        db.query(models.Message)
        .options(joinedload(models.Message.sender))
        .filter(models.Message.conversation_id == conversation_id)
        .order_by(models.Message.created_at.asc())
        .all()
    )


def create_message(
    db: Session, conversation_id: int, payload: schemas.MessageCreate
) -> models.Message | None:
    conversation = db.get(models.Conversation, conversation_id)
    sender = db.get(models.User, payload.sender_id)
    if conversation is None or sender is None:
        return None

    is_participant = (
        db.query(models.ConversationParticipant)
        .filter(
            models.ConversationParticipant.conversation_id == conversation_id,
            models.ConversationParticipant.user_id == payload.sender_id,
        )
        .first()
    )
    if is_participant is None:
        return None

    message = models.Message(
        content=payload.content.strip(),
        conversation_id=conversation_id,
        sender_id=payload.sender_id,
    )
    db.add(message)
    db.commit()
    db.refresh(message)
    return (
        db.query(models.Message)
        .options(joinedload(models.Message.sender))
        .filter(models.Message.id == message.id)
        .first()
    )


def update_message(
    db: Session, message_id: int, payload: schemas.MessageUpdate
) -> models.Message | None:
    message = db.get(models.Message, message_id)
    if message is None:
        return None
    message.content = payload.content.strip()
    db.commit()
    db.refresh(message)
    return (
        db.query(models.Message)
        .options(joinedload(models.Message.sender))
        .filter(models.Message.id == message.id)
        .first()
    )


def delete_message(db: Session, message_id: int) -> bool:
    message = db.get(models.Message, message_id)
    if message is None:
        return False
    db.delete(message)
    db.commit()
    return True
