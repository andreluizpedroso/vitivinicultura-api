# app/main.py
from fastapi import FastAPI
from .routers import producao, processamento, comercializacao, importacao, exportacao

app = FastAPI(
    title="API Vitivinicultura Embrapa",
    description="API para consultar dados de vitivinicultura do site da Embrapa",
    version="1.0.0"
)

app.include_router(producao.router, prefix="/api/v1")
app.include_router(processamento.router, prefix="/api/v1")
app.include_router(comercializacao.router, prefix="/api/v1")
app.include_router(importacao.router, prefix="/api/v1")
app.include_router(exportacao.router, prefix="/api/v1")