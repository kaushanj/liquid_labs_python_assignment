from fastapi import APIRouter, Depends

from controllers.symbols import SymbolController
from repositories.symbols import Symbolerepository
from clients.alphavantage import AlphaVantageClient
from .schema import validate_symbol, validate_year

from core.db import get_db

router = APIRouter(prefix="/symbols", tags=["symbols"])


def get_symbol_controller(db = Depends(get_db)):
    return SymbolController(repository=Symbolerepository(db), client=AlphaVantageClient())

@router.get("/{symbol}/annual/{year}", response_model= dict[str, str])
def get_symbol_summery(symbol: str = Depends(validate_symbol), year: int = Depends(validate_year), 
                       controller: SymbolController = Depends(get_symbol_controller)):

    return controller.get_summary(symbol, year)