from typing import List, TYPE_CHECKING
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, func, Boolean

from src.configs.app_config import app_settings

if TYPE_CHECKING:
    from .todo_model import TodoModel


class UserModel(app_settings.BASE):
    __tablename__: str = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(String(355), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )
    is_active: Mapped[Boolean] = mapped_column(Boolean, default=True, nullable=False)
    todos: Mapped[List["TodoModel"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
