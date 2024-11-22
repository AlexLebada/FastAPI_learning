from typing import Optional
from starlette.requests import Request
from view_models.shared import ViewModelBase
from controllers.strava import assess_target



class TargetStatusViewModel(ViewModelBase):
    def __init__(self,request):
        # Calls ViewModelBase.__init__(self, request)
        super().__init__(request)
        self.target: Optional[str] = ""
        self.kms: Optional[str] = ""
        self.message: Optional[str] = None

    async def load(self):
        # .form() is async method provided by starlette Request class
        form = await self.request.form()
        self.target = form.get('target')
        self.kms = form.get('kilometers')

    def assess_target(self):
        self.message = assess_target(int(self.kms), int(self.target))
