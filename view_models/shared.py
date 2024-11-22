### this view is shared with all view models

from starlette.requests import Request

class ViewModelBase:
    # : Request is a type hint that expects Request object
    def __init__(self, request: Request) -> None:
        self.request: Request = request

    # converts instance into a dictionary
    def to_dict(self) -> dict:
        # __dict__ built-in attribute in Python
        return self.__dict__