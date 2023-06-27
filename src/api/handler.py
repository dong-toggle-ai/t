import logging

from fastapi import Request
from fastapi import Response
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from starlette import status
from starlette.responses import JSONResponse

from exceptions.exceptions import InternalServerError
from exceptions.exceptions import NoContentError

logger = logging.getLogger("handler")


async def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"Uncaught exception {exc}", exc_info=exc)

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=jsonable_encoder({"message": "Internal server error. Please try again later."}),
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.warning(f"Invalid schema {request.url.path}", exc_info=exc)

    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"message": exc.errors()}),
    )


async def internal_server_handler(request: Request, exc: InternalServerError):
    logger.warning(f"Internal server error for {request.url.path}", exc_info=False)

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=jsonable_encoder({"message": exc.message}),
    )


async def no_content_handler(request: Request, exc: NoContentError):
    logger.warning(f"No content {request.url.path}: {exc.message}", exc_info=False)

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )
