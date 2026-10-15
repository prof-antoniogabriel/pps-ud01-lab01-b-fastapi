from typing import Literal

from pydantic import BaseModel, Field


class NoticeCreate(BaseModel):
    title: str = Field(min_length=3, max_length=120)
    severity: Literal["low", "medium", "high"]


class NoticeRead(NoticeCreate):
    id: int
