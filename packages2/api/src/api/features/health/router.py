from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class HealthResponse(BaseModel):
    status: str
    message: str


@router.get("/healthz", response_model=HealthResponse)
async def health_check():
    return HealthResponse(status="ok", message="Service is healthy")
