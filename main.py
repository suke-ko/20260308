from fastapi import FastAPI,  Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        'index.html',
        {
            'request': request
        }
    )


@app.get('/update_color', response_class=HTMLResponse)
async def update_color(
    request: Request,
    r: int = 0,
    g: int = 0,
    b: int = 0
):
    return templates.TemplateResponse(
        'display.html',
        {
            'request': request,
            'r': r,
            'g': g,
            'b': b
        }
    )
