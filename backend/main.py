import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Cria a instância da aplicação FastAPI
app = FastAPI()

# Definição dos caminhos para servir os arquivos estáticos
# PASTA_BASE obtém o diretório do arquivo main.py
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))

# PASTA_IMAGENS aponta para a pasta "figurinhas" dentro do mesmo diretório
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Configuração dos arquivos estáticos: monta a pasta local na rota "/imgs"
app.mount("/imgs", StaticFiles(directory=PASTA_IMAGENS), name="imgs")

# Lista de figurinhas contendo os dados e a URL das imagens servidas estaticamente
figurinhas = [
    {
        "id": 1, 
        "nome": "Alan Turing", 
        "categoria": "IA", 
        "imagem_url": "/imgs/01-alan-turing.jpg"
    },
    {
        "id": 2, 
        "nome": "John McCarthy", 
        "categoria": "IA", "imagem_url": 
        "/imgs/02-john-mccarthy.jpg"
    }
]

# Endpoint único: GET "/figurinhas" que retorna a lista completa de figurinhas
@app.get("/figurinhas")
def listar_figurinhas():
    # Retorna a lista de dicionários contendo as figurinhas de exemplo
    return figurinhas

