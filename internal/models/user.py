
from sqlalchemy.orm import mapped_column
from sqlalchemy import (
    Integer,
    Boolean,
    String,
    LargeBinary,
    UUID,
    DateTime,
    ForeignKey
)

from internal.models.base import Base


class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    telegram_id = mapped_column(Integer, unique=True, nullable=False)
    is_admin = mapped_column(Boolean, default=False, server_default="false", nullable=False)
    
    date_created = mapped_column(DateTime, nullable=False)
    date_updated = mapped_column(DateTime, nullable=False)
    data_deleted = mapped_column(DateTime, nullable=False)