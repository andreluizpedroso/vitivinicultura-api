# app/routers/processamento.py
from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from ..utils.data_fetcher import fetch_data_from_embrapa

router = APIRouter()

# Dicionário para mapear o filtro com a URL correspondente
URLS_PROCESSAMENTO = {
    "viniferas": "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03",
    "americanas_e_hibridas": "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_03",
    "uvas_de_mesa": "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_03",
    "sem_classificacao": "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_03"
}

@router.get("/processamento")
async def get_processamento(
    filtro: str = Query("viniferas", enum=list(URLS_PROCESSAMENTO.keys())),
    ano: Optional[int] = Query(2023, ge=1970, le=2023)
):
    """
    Endpoint para consultar dados de processamento com diferentes filtros e ano.
    
    Parâmetros:
    - filtro: Tipo de filtro a ser aplicado. Pode ser um dos seguintes:
        - viniferas
        - americanas_e_hibridas
        - uvas_de_mesa
        - sem_classificacao
    - ano: Ano para filtrar os dados, de 1970 a 2023.
    """
    url = URLS_PROCESSAMENTO.get(filtro)
    # Adiciona o ano à URL como parâmetro de consulta
    if ano:
        url += f"&ano={ano}"
    try:
        data = await fetch_data_from_embrapa(url)
        return {"data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
