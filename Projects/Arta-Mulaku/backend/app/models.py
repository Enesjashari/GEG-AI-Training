from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    sent_messages: Mapped[list["Message"]] = relationship(
        back_populates="sender", cascade="all, delete-orphan"
    )
    memberships: Mapped[list["ConversationParticipant"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )


class Conversation(Base):
    __tablename__ = "conversations"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(150))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    participants: Mapped[list["ConversationParticipant"]] = relationship(
        back_populates="conversation", cascade="all, delete-orphan"
    )
    messages: Mapped[list["Message"]] = relationship(
        back_populates="conversation", cascade="all, delete-orphan"
    )


class ConversationParticipant(Base):
    __tablename__ = "conversation_participants"

    id: Mapped[int] = mapped_column(primary_key=True)
    conversation_id: Mapped[int] = mapped_column(ForeignKey("conversations.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    conversation: Mapped["Conversation"] = relationship(back_populates="participants")
    user: Mapped["User"] = relationship(back_populates="memberships")


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    conversation_id: Mapped[int] = mapped_column(ForeignKey("conversations.id"))
    sender_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    conversation: Mapped["Conversation"] = relationship(back_populates="messages")
    sender: Mapped["User"] = relationship(back_populates="sent_messages")
