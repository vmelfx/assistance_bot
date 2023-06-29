class DatabaseError(Exception):
    def __init__(self) -> None:
        return super().__init__("Something went wrong.\n Please try again")
