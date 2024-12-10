
# Vitivinicultura API

## 📚 Descrição do Projeto
A **Vitivinicultura API** é uma aplicação desenvolvida em Python utilizando o framework **FastAPI**. Esta API permite consultas de dados do site da Embrapa relacionados à produção, processamento, comercialização, importação e exportação de produtos vitivinícolas. Os dados serão utilizados futuramente para alimentar um modelo de Machine Learning.

---

## 🚀 Funcionalidades
- **Consulta de dados de produção**: Obtenha informações sobre a produção vitivinícola.
- **Consulta de dados de processamento**: Dados relacionados ao processamento de uvas e vinhos.
- **Consulta de dados de comercialização**: Informações sobre vendas e mercado.
- **Consulta de dados de importação e exportação**: Dados sobre o comércio internacional de produtos vitivinícolas.

---

## 🛠️ Tecnologias Utilizadas
- **Python** (versão 3.12.4)
- **FastAPI** (framework principal para APIs)
- **Uvicorn** (servidor ASGI)
- **Requests** ou **HTTPX** (para consultas ao site da Embrapa)
- **Mangum** (para deploy na Vercel)

---

## 📖 Instalação e Uso Local

### Pré-requisitos
- **Python 3.9+**
- **Git** instalado
- Ambiente virtual configurado

### Passo a Passo
1. Clone o repositório:
   ```bash
   git clone https://github.com/andreluizpedroso/vitivinicultura-api.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd vitivinicultura-api
   ```
3. Crie e ative um ambiente virtual:
   ```bash
   python -m venv env
   .\env\Scripts\activate  # No Windows
   source env/bin/activate # No Linux/Mac
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Rode o servidor localmente:
   ```bash
   uvicorn app.main:app --reload
   ```
6. Acesse a API:
   - **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - **Redoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🌐 Deploy
A API está implantada e acessível em:
- **Vercel**: [https://vitivinicultura-api.vercel.app](https://vitivinicultura-api.vercel.app).

---

## 📂 Estrutura do Projeto
```plaintext
project/
├── app/
│   ├── __init__.py
│   ├── main.py               # Configuração principal da API
│   ├── routers/              # Rotas organizadas por funcionalidade
│   │   ├── __init__.py
│   │   ├── producao.py
│   │   ├── processamento.py
│   │   ├── comercializacao.py
│   │   ├── importacao.py
│   │   ├── exportacao.py
│   ├── utils/                # Funções utilitárias
│       ├── __init__.py
│       ├── data_fetcher.py   # Scripts para consultas na Embrapa
├── env/                      # Ambiente virtual
├── requirements.txt          # Dependências do projeto
├── vercel.json               # Configurações para deploy na Vercel
├── README.md                 # Documentação do projeto
```

---

## 📌 Endpoints da API
| Método | Endpoint           | Descrição                                |
|--------|--------------------|------------------------------------------|
| `GET`  | `/producao`        | Retorna dados de produção.               |
| `GET`  | `/processamento`   | Retorna dados de processamento.          |
| `GET`  | `/comercializacao` | Retorna dados de comercialização.        |
| `GET`  | `/importacao`      | Retorna dados de importação.             |
| `GET`  | `/exportacao`      | Retorna dados de exportação.             |

---

## 👥 Contribuidores
- **André Luiz Pedroso** - Desenvolvedor principal

---
