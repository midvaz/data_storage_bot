
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


class Message_hub(Base):
    __tablename__ = "message_hub"

    id = mapped_column(Integer, primary_key=True)
    user_id = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    tag_id = mapped_column(ForeignKey("tags.id", ondelete="CASCADE"))
    descrition = mapped_column(String, unique=True, nullable=False)
    body_data = mapped_column(String, unique=True, nullable=False)
    
    date_created = mapped_column(DateTime, nullable=False)
    date_updated = mapped_column(DateTime, nullable=False)
    data_deleted = mapped_column(DateTime, nullable=False)