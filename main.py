from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Pasta de arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="public")  # ou templates se você usa templates

# Rotas GET
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
def contato_get(request: Request):
    return templates.TemplateResponse("contato.html", {"request": request})

# Nova rota POST
@app.post("/contato")
def contato_post(
    nome: str = Form(...),
    email: str = Form(...),
    mensagem: str = Form(...)
):
    # Aqui você pode salvar no banco ou enviar e-mail
    print(f"Contato recebido: {nome}, {email}, {mensagem}")
    return JSONResponse({"status": "sucesso", "mensagem": "Contato recebido!"})
