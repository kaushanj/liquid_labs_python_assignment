
from fastapi import status

class CustomException(Exception):
    code = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = "Internal Server Error."

    def __init__(self, message=None):
        if message:
            self.message = message


class NotFoundException(CustomException):
    message = "No data found for this symbol or year."
    code = status.HTTP_404_NOT_FOUND

class ProviderException(CustomException):
    message = "Market data provider unavailable."
    code = status.HTTP_503_SERVICE_UNAVAILABLE

class ConfigException(CustomException):
    message = "API key is not set."
    code = status.HTTP_503_SERVICE_UNAVAILABLE


class ValidationException(CustomException):
    message = "Invalid data provided."
    code = status.HTTP_400_BAD_REQUEST


