import dotenv 
dotenv.load_dotenv()

from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exception_handlers import http_exception_handler
from api.symbols import router as symbol_router

from core import db
from core.exception import CustomException



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


@app.exception_handler(CustomException)
async def on_custom_validation(_: Request, exc: CustomException):
    return JSONResponse(status_code=exc.code, content={"detail": exc.message})


@app.exception_handler(Exception)
async def unhandled_exception(request: Request, exc: Exception):
    if isinstance(exc, HTTPException):
        return await http_exception_handler(request, exc)

    return JSONResponse(status_code=500, content={"detail": "Internal Server Error."})


