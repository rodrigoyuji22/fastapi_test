from threading import ExceptHookArgs


class UserNotFoundError(Exception):
    pass

class PasswordValidationError(Exception):
    pass

class UserAlreadyExistsError(Exception):
    pass
    
class InvalidCredentialsError(Exception):
    pass
