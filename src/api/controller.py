import logging

from fastapi import APIRouter, Response

logger = logging.getLogger(__name__)
api_router = APIRouter()


@api_router.get("/health-check")
async def health_check():
    return Response(content="ok")
