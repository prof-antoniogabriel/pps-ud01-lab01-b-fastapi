from fastapi import APIRouter, HTTPException, status

from app.core.config import settings
from app.schemas.notice import NoticeCreate, NoticeRead
from app.services.notice_service import create_notice, get_notice, list_notices

router = APIRouter(prefix="/notices", tags=["notices"])


@router.get("/", response_model=list[NoticeRead])
def read_notices() -> list[NoticeRead]:
    return list_notices(limit=settings.notice_limit)


@router.get("/{notice_id}", response_model=NoticeRead)
def read_notice(notice_id: int) -> NoticeRead:
    notice = get_notice(notice_id)
    if notice is None:
        raise HTTPException(status_code=404, detail="Aviso no encontrado")
    return notice


@router.post("/", response_model=NoticeRead, status_code=status.HTTP_201_CREATED)
def add_notice(payload: NoticeCreate) -> NoticeRead:
    return create_notice(payload)
