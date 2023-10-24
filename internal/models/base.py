
from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")