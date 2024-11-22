from typing import Optional
from starlette.requests import Request
from view_models.shared import ViewModelBase

class UserLoginViewModel(ViewModelBase):
    def __init__(self, request: Request) -> None:
        super().__init__(request)
        self.username: Optional[str] = None
        self.password: Optional[str] = None
        self.message: Optional[str] = None

    async def load(self):
        form = await self.request.form()
        self.username = form.get("username")
        self.password = form.get("password")