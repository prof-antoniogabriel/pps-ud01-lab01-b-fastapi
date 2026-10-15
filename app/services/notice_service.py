from app.schemas.notice import NoticeCreate, NoticeRead

# Almacenamiento en memoria: se reinicia al detener la aplicación.
_notices: dict[int, NoticeRead] = {
    1: NoticeRead(id=1, title="Revisar accesos", severity="medium"),
    2: NoticeRead(id=2, title="Actualizar dependencias", severity="high"),
}
_next_id = 3


def list_notices(limit: int = 50) -> list[NoticeRead]:
    return list(_notices.values())[:limit]


def get_notice(notice_id: int) -> NoticeRead | None:
    return _notices.get(notice_id)


def create_notice(payload: NoticeCreate) -> NoticeRead:
    global _next_id
    notice = NoticeRead(id=_next_id, **payload.model_dump())
    _notices[_next_id] = notice
    _next_id += 1
    return notice
