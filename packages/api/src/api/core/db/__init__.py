import uuid
from datetime import datetime
from typing import ClassVar, Any

from sqlalchemy import Column, DateTime, func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import JSON, MetaData
from sqlalchemy.types import TypeEngine


class Base(DeclarativeBase):
    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )

    type_annotation_map: ClassVar[dict[type, TypeEngine[Any]]] = {
        datetime: DateTime(timezone=True),
        dict[str, str]: JSON(),
    }


class HasId:
    id = Column(
        "id",
        TypeEngine[uuid.UUID],
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    __mapper_args__ = {"eager_defaults": True}  # type: ignore[misc]


class HasTimestamp:
    created_at = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at = Column(
        DateTime(timezone=True),
        nullable=True,
        onupdate=func.now(),
        server_default=func.now(),
    )
