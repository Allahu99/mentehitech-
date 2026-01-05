from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Pasta de arquivos estáticos (CSS, JS, imagens)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates HTML
templates = Jinja2Templates(directory="templates")

# Rotas
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/servicos", response_class=HTMLResponse)
def servicos(request: Request):
    return templates.TemplateResponse("servicos.html", {"request": request})

@app.get("/precos", response_class=HTMLResponse)
def precos(request: Request):
    return templates.TemplateResponse("precos.html", {"request": request})

@app.get("/contato", response_class=HTMLResponse)
def contato(request: Request):
    return templates.TemplateResponse("contato.html", {"request": request})
from fastapi import Form
from fastapi.responses import RedirectResponse

@app.post("/contato")
def enviar_contato(
    nome: str = Form(...),
    email: str = Form(...),
    mensagem: str = Form(...)
):
    print("Novo contato:", nome, email, mensagem)
    return RedirectResponse(url="/contato", status_code=303)
