from database import Base
from sqlalchemy.orm import Mapped, mapped_column
import uuid # is a 16 byte (128 bit) number that is used to identify information in computer systems. The term "UUID" stands for "Universally Unique Identifier," and it is designed to be unique across both time and space, making it an ideal choice for generating unique identifiers for various applications.
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String, DateTime, Text, Integer #if needed
from datetime import datetime, timezone

class urls(Base):

    __tablename__ = "URLS"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid = True),
        primary_key= True,
        default=uuid.uuid4
    )

    original_url:Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False
    )
    short_code:Mapped[str] = mapped_column(
        String(32),
        unique=True,
        index=True,
        nullable=False
    )
    click_count:Mapped[int] = mapped_column(
        Integer,
        index=True,
        default=0
    )
    created_at:Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    #relationship to be declared if any
