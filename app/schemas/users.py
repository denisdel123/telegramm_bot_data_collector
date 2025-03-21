from pydantic import BaseModel, Field
from typing import Optional


class TelegramUserCreate(BaseModel):
    id: int
    username: Optional[str] = Field(None, description="Имя пользователя")
    first_name: Optional[str] = Field(None, description="Имя")
    language_code: Optional[str] = Field(None, description="Язык пользователя")
    chat_id: int
    chat_type: str


class TelegramUserResponse(TelegramUserCreate):
    created_at: str

