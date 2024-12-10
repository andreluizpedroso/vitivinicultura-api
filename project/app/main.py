# app/main.py
from fastapi import FastAPI
from mangum import Mangum  # Importando o adaptador Mangum
from .routers import producao, processamento, comercializacao, importacao, exportacao

import sys
import logging

logging.basicConfig(level=logging.INFO)
logging.info(f"Versão do Python em execução: {sys.version}")

app = FastAPI(
    title="API Vitivinicultura Embrapa",
    description="API para consultar dados de vitivinicultura do site da Embrapa",
    version="1.0.0"
)

# Endpoint principal (raiz da API)
@app.get("/")
async def root():
    return {"message": "API Vitivinicultura Embrapa funcionando na Vercel!"}

# Incluindo os roteadores
app.include_router(producao.router, prefix="/api/v1")
app.include_router(processamento.router, prefix="/api/v1")
app.include_router(comercializacao.router, prefix="/api/v1")
app.include_router(importacao.router, prefix="/api/v1")
app.include_router(exportacao.router, prefix="/api/v1")

# Handler para o ambiente serverless
handler = Mangum(app)
