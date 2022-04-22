from abc import ABC
from typing import Optional
from .serializers import ExceptionSerializer


class CommonExceptions(Exception, ABC):
    status_code: int = 400
    code: str = NotImplemented
    error: Optional[str]
    response: Optional[str]

    def __init__(
        self,
        error: Optional[str] = None,
        response: Optional[str] = None
    ):
        Exception.__init__(self)
        self.error = error
        self.response = response

    def to_dict(self):
        return ExceptionSerializer(
            code=self.code,
            error=self.error,
            response=self.response,
        ).dict()
