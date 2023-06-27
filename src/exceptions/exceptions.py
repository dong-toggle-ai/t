class BaseError(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message


class NoContentError(BaseError):
    def __init__(self, message: str):
        super().__init__(status_code=204, message=message)


class InternalServerError(BaseError):
    def __init__(self, message: str):
        super().__init__(status_code=500, message=message)
