# app/routers/producao.py
from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from ..utils.data_fetcher import fetch_data_from_embrapa

router = APIRouter()

# URL base para a rota de produção
URL_PRODUCAO = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02"

@router.get("/producao")
async def get_producao(ano: Optional[int] = Query(2023, ge=1970, le=2023)):
    """
    Endpoint para consultar dados de produção com filtro de ano.
    
    Parâmetros:
    - ano: Ano para filtrar os dados, de 1970 a 2023.
    """
    # Adiciona o ano à URL como parâmetro de consulta
    url = f"{URL_PRODUCAO}&ano={ano}"
    
    try:
        data = await fetch_data_from_embrapa(url)
        return {"data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
