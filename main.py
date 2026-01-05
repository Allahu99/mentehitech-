from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()

# Montar arquivos estáticos (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates (se você quiser usar jinja2)
templates = Jinja2Templates(directory="public")

# Rotas GET para as páginas
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/servicos", response_class=HTMLResponse)
async def servicos(request: Request):
    return templates.TemplateResponse("servicos.html", {"request": request})

@app.get("/precos", response_class=HTMLResponse)
async def precos(request: Request):
    return templates.TemplateResponse("precos.html", {"request": request})

@app.get("/contato", response_class=HTMLResponse)
async def contato(request: Request):
    return templates.TemplateResponse("contato.html", {"request": request})

# Rota POST para receber formulário de contato
@app.post("/contato")
async def receber_contato(
    nome: str = Form(...),
    email: str = Form(...),
    mensagem: str = Form(...)
):
    print(f"Recebido: {nome}, {email}, {mensagem}")
    return JSONResponse({"status": "sucesso", "mensagem": "Contato recebido!"})
