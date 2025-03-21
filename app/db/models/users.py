from sqlalchemy import Integer, String, DateTime, Column
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TelegramUser(Base):
    __tablename__ = "telegram_user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=True, unique=True)
    first_name = Column(String, nullable=True)
    language_code = Column(String(10), nullable=True)
    chat_id = Column(Integer, unique=True)
    chat_type = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

