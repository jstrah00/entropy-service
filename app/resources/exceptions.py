class MissingFileException(Exception):
    def __init__(self, message: str = "Required file missing") -> None:
        self.__status_code = 400
        self.message = message

    def get_status_code(self) -> int:
        return self.__status_code

    def get_exception_message(self) -> str:
        return self.message
