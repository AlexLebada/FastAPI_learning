import fastapi
from fastapi.responses import HTMLResponse
from starlette.requests import Request
# template engine for dynamic web pages
from fastapi.templating import Jinja2Templates
from fastapi import status
from view_models.target_strava import TargetStatusViewModel
from fastapi import Request, Form, status
from fastapi.responses import RedirectResponse

router_2 = fastapi.APIRouter()

templates = Jinja2Templates(directory="templates")

@router_2.get("/", response_class=HTMLResponse, include_in_schema=False)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router_2.post("/login", response_class=HTMLResponse, include_in_schema=False)
async def process_login(request: Request, username: str = Form(...), password: str = Form(...)):
    # Replace this with actual authentication logic
    if username == "admin" and password == "password123":
        response = RedirectResponse(url="/form", status_code=status.HTTP_302_FOUND)
        response.set_cookie(key="logged_in", value="true")  # Simulating a logged-in user
        print("yes")
        return response
    else:
        print("no")
        return templates.TemplateResponse("login.html", {
            "request": request,
            "error": "Invalid username or password."
        })

@router_2.get("/form", response_class=HTMLResponse, include_in_schema=False) # response_class treat response as HTML content instead of JSON
async def form(request: Request):
    if not request.cookies.get("logged_in"):
        return RedirectResponse(url="/")
    vm = TargetStatusViewModel(request)
    return templates.TemplateResponse("/index.html", vm.to_dict())
    #return "<h1> Hello </h1"

@router_2.post("/form", response_class=HTMLResponse, include_in_schema=False)
async def form(request: Request):
    if not request.cookies.get("logged_in"):
        return RedirectResponse(url="/login")
    vm = TargetStatusViewModel(request)
    await vm.load()
    vm.assess_target()
    print(vm.to_dict())
    params = f"?kms={vm.kms}&target={vm.target}&message={vm.message}"
    response = fastapi.responses.RedirectResponse(f"/target_status{params}", status_code=status.HTTP_302_FOUND)
    return response

@router_2.get("/target_status", response_class=HTMLResponse, include_in_schema=False)
def target_status(request: Request, target: str, kms:str):
    if not request.cookies.get("logged_in"):
        return RedirectResponse(url="/")
    vm = TargetStatusViewModel(request)
    vm.kms = kms
    vm.target = target
    vm.assess_target()
    print(vm.to_dict())
    return templates.TemplateResponse("/target_status.html", vm.to_dict())

@router_2.post("/logout", response_class=HTMLResponse, include_in_schema=False)
async def logout(request: Request):
    response = RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
    response.delete_cookie("logged_in")  # This will remove the 'logged_in' cookie
    return response