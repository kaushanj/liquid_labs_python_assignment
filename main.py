from fastapi import FastAPI
from contextlib import asynccontextmanager
from api.symbols import router as symbol_router

from core import db


@asynccontextmanager
async def lifespan(app: FastAPI):
    db.create_market_data_table()
    yield

app = FastAPI(
    title="Alpha Vantage Stock",
    description="Python Assignment",
    lifespan=lifespan
)

app.include_router(symbol_router)


