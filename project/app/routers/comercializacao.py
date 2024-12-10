# app/routers/comercializacao.py
from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from ..utils.data_fetcher import fetch_data_from_embrapa

router = APIRouter()

# URL base para a rota de comercialização
URL_COMERCIALIZACAO = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04"

@router.get("/comercializacao")
async def get_comercializacao(ano: Optional[int] = Query(2023, ge=1970, le=2023)):
    """
    Endpoint para consultar dados de comercialização com filtro de ano.
    
    Parâmetros:
    - ano: Ano para filtrar os dados, de 1970 a 2023.
    """
    # Adiciona o ano à URL como parâmetro de consulta
    url = f"{URL_COMERCIALIZACAO}&ano={ano}"
    
    try:
        data = await fetch_data_from_embrapa(url)
        return {"data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
