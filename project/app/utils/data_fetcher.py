# app/utils/data_fetcher.py
import httpx
from bs4 import BeautifulSoup

async def fetch_data_from_embrapa(url: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()  # Verifica erros na resposta
        
        # Processa o HTML usando BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extraindo todas as tabelas da página
        tables = soup.find_all('table')
        
        # Estrutura para armazenar os dados das tabelas
        data = {}

        for i, table in enumerate(tables):
            table_data = []
            # Pega todas as linhas da tabela
            rows = table.find_all('tr')
            # Extrai o cabeçalho da tabela (se houver)
            headers = [header.get_text(strip=True) for header in rows[0].find_all('th')] if rows[0].find_all('th') else None

            # Itera sobre as linhas, pulando o cabeçalho se ele existir
            for row in rows[1:] if headers else rows:
                cells = row.find_all('td')
                row_data = [cell.get_text(strip=True) for cell in cells]
                
                # Se houver cabeçalho, cria um dicionário para cada linha usando os cabeçalhos como chaves
                if headers:
                    table_data.append(dict(zip(headers, row_data)))
                else:
                    table_data.append(row_data)

            # Adiciona os dados da tabela no dicionário final
            data[f'table_{i+1}'] = table_data
        
        return data
