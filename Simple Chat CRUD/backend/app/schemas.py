from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class UserBase(BaseModel):
    name: str = Field(min_length=1, max_length=100)


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserRead(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime


class ParticipantRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str


class ConversationBase(BaseModel):
    title: str = Field(min_length=1, max_length=150)


class ConversationCreate(ConversationBase):
    participant_ids: list[int] = Field(min_length=2)


class ConversationUpdate(ConversationBase):
    participant_ids: list[int] = Field(min_length=2)


class ConversationRead(ConversationBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    participants: list[ParticipantRead]


class MessageCreate(BaseModel):
    sender_id: int
    content: str = Field(min_length=1)


class MessageUpdate(BaseModel):
    content: str = Field(min_length=1)


class MessageRead(BaseModel):
    id: int
    content: str
    created_at: datetime
    conversation_id: int
    sender: ParticipantRead

    model_config = ConfigDict(from_attributes=True)
