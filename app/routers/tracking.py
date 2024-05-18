from fastapi import APIRouter
from ..tasks import fetch_tracking_info

router = APIRouter()


@router.get("/track/{tracking_number}")
async def track_package(tracking_number: str):
    task = fetch_tracking_info.apply_async(args=[tracking_number])
    return {"task_id": task.id, "status": "Task has been submitted"}
