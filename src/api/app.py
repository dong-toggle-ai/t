import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from api.config import config
from api.controller import api_router
from api.handler import general_exception_handler
from api.handler import internal_server_handler
from api.handler import no_content_handler
from api.handler import validation_exception_handler
from exceptions.exceptions import InternalServerError
from exceptions.exceptions import NoContentError

app = FastAPI()
app.include_router(api_router)
app.add_exception_handler(InternalServerError, internal_server_handler)
app.add_exception_handler(Exception, general_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(NoContentError, no_content_handler)

if __name__ == "__main__":
    uvicorn.run("app:app", log_level=config.LOG_LEVEL)
