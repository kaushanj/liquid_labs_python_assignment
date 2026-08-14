from fastapi import FastAPI

from api.symbols import router as symbol_router

app = FastAPI(
    title="Alpha Vantage Stock",
    description="Python Assignment"
)

app.include_router(symbol_router)

