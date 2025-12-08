from fastapi import FastAPI
from core.exceptions import PasswordValidationError, UserAlreadyExistsError, UserNotFoundError
from fastapi.responses import JSONResponse

def register_exceptions_handlers(app: FastAPI):
    @app.exception_handler(PasswordValidationError)
    def password_error_handler(_, exc):
        return JSONResponse(status_code=422, content={"detail": str(exc)})

    @app.exception_handler(UserNotFoundError)
    def user_not_found_handler(_, exc):
        return JSONResponse(status_code=404, content={"detail": str(exc)})

    @app.exception_handler(UserAlreadyExistsError)
    def user_already_exists(_, exc):
        return JSONResponse(status_code=422, content={ "detail": str(exc)})