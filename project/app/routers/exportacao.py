# app/routers/exportacao.py
from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from ..utils.data_fetcher import fetch_data_from_embrapa

router = APIRouter()

# Dicionário para mapear o filtro com a URL base correspondente
URLS_EXPORTACAO = {
    "vinhos_de_mesa": "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06",
    "espumantes": "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_06",
    "uvas_frescas": "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_06",
    "suco_de_uva": "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_06"
}

@router.get("/exportacao")
async def get_exportacao(
    filtro: str = Query("vinhos_de_mesa", enum=list(URLS_EXPORTACAO.keys())),
    ano: Optional[int] = Query(2023, ge=1970, le=2023)
):
    """
    Endpoint para consultar dados de exportação com diferentes filtros e ano.
    
    Parâmetros:
    - filtro: Tipo de filtro a ser aplicado. Pode ser um dos seguintes:
        - vinhos_de_mesa
        - espumantes
        - uvas_frescas
        - suco_de_uva
    - ano: Ano para filtrar os dados, de 1970 a 2023.
    """
    url = URLS_EXPORTACAO.get(filtro)
    # Adiciona o ano à URL como parâmetro de consulta
    if ano:
        url += f"&ano={ano}"
    try:
        data = await fetch_data_from_embrapa(url)
        return {"data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
