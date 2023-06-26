
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

from base import Base


class Tag(Base):
    __tablename__ = "tags"

    user_id = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    name = mapped_column(String, unique=True, nullable=False)
    
    date_created = mapped_column(DateTime, nullable=False)
    date_updated = mapped_column(DateTime, nullable=False)
    data_deleted = mapped_column(DateTime, nullable=False)