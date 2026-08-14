# Liquid Labs Python Assignment

Simple FastAPI app for Liquid Labs Python Assignment

## Setup 
```bash 
curl -LsSf https://astral.sh/uv/install.sh | sh 
source $HOME/.local/bin/env 
uv sync 
cp .env.example .env
```

## Run 

```bash 
uv run uvicorn main:app --reload
```

Set in `.env`

- ALPHAVANTAGE_API_KEY=your_key
- DB_PATH=market.db (optional)

## Usage

```

curl  http://127.0.0.1:8000/symbols/IBM/annual/2005 

```


## Database

By default DB is `market.db` if you do not set the path in `.env`.


## Libraries

- requests — Alpha Vantage HTTP call 
- python-dotenv — load .env