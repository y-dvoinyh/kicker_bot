"""User model file."""
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Mapped, mapped_column

from src.bot.structures.role import Role

from .base import BaseModel
from .chat import ChatModel


class UserModel(BaseModel):
    """User model."""
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(sa.BigInteger, autoincrement=True, primary_key=True)
    # Telegram user id
    user_id: Mapped[int] = mapped_column(
        sa.BigInteger, unique=True, nullable=False
    )
    # Telegram user name
    user_name: Mapped[str] = mapped_column(
        sa.Text, unique=False, nullable=True
    )
    # Telegram profile first name
    first_name: Mapped[str] = mapped_column(
        sa.Text, unique=False, nullable=True
    )
    # Telegram profile second name
    second_name: Mapped[str] = mapped_column(
        sa.Text, unique=False, nullable=True
    )
    # Telegram user premium status
    is_premium: Mapped[bool] = mapped_column(
        sa.Boolean, unique=False, nullable=False
    )
    # User's role
    role: Mapped[Role] = mapped_column(sa.Enum(Role), default=Role.USER)
    # Telegram chat with user
    user_chat_fk: Mapped[int] = mapped_column(
        sa.ForeignKey('chat.id'), unique=False, nullable=False
    )
    user_chat: Mapped[ChatModel] = orm.relationship(
        'Chat', uselist=False, lazy='joined'
    )
