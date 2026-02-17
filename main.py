from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Arquivos estáticos (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates ou HTMLs
templates = Jinja2Templates(directory="public")  # se suas páginas estão em public/

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

# Rota POST /contato
@app.post("/contato")
def contato_post(nome: str = Form(...), email: str = Form(...), mensagem: str = Form(...)):
    print(f"[CONTATO RECEBIDO] Nome: {nome}, Email: {email}, Mensagem: {mensagem}")
    # Aqui você pode salvar em DB ou enviar email
    return {"status": "sucesso", "mensagem": "Contato recebido!"}
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

templates = Jinja2Templates(directory="templates")

@app.get("/checkout", response_class=HTMLResponse)
async def checkout(request: Request):
    return templates.TemplateResponse("checkout.html", {"request": request})
