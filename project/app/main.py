from fastapi import FastAPI
from mangum import Mangum 
from .routers import producao, processamento, comercializacao, importacao, exportacao
from fastapi.openapi.utils import get_openapi

tags_metadata = [
    {
        "name": "Principal",
        "description": "Endpoints principais e informações básicas da API.",
    },
    {
        "name": "Produção",
        "description": "Endpoints relacionados à produção vitivinícola.",
    },
    {
        "name": "Processamento",
        "description": "Endpoints sobre etapas de processamento vitivinícola.",
    },
    {
        "name": "Comercialização",
        "description": "Endpoints para dados de comercialização.",
    },
    {
        "name": "Importação",
        "description": "Dados sobre importação de produtos vitivinícolas.",
    },
    {
        "name": "Exportação",
        "description": "Dados sobre exportação de produtos vitivinícolas.",
    },
]

app = FastAPI(
    title="API Vitivinicultura Embrapa",
    description=(
        "API para acessar informações relacionadas à vitivinicultura com dados oriundos do site da Embrapa. "
        "Disponibiliza informações sobre produção, processamento, comercialização, importação e exportação de produtos vitivinícolas."
    ),
    version="1.0.0",
    openapi_tags=tags_metadata,
)

# Personalização do Swagger UI
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="API Vitivinicultura Embrapa",
        version="1.0.0",
        description="Documentação completa da API Vitivinicultura Embrapa.",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# Endpoint principal (raiz da API)
@app.get(
    "/",
    tags=["Principal"],
    summary="Endpoint principal",
    description="Verifica se a API está operacional e retorna uma mensagem de boas-vindas."
)
async def root():
    return {"message": "API Vitivinicultura Embrapa funcionando!"}

# Incluindo os roteadores
app.include_router(producao.router, prefix="/api/v1", tags=["Produção"])
app.include_router(processamento.router, prefix="/api/v1", tags=["Processamento"])
app.include_router(comercializacao.router, prefix="/api/v1", tags=["Comercialização"])
app.include_router(importacao.router, prefix="/api/v1", tags=["Importação"])
app.include_router(exportacao.router, prefix="/api/v1", tags=["Exportação"])

# Handler para o ambiente serverless
handler = Mangum(app)
