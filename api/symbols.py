from fastapi import APIRouter, Depends

from controllers.symbols import SymbolController
from .schema import validate_symbol, validate_year
router = APIRouter(prefix="/symbols", tags=["symbols"])


def get_symbol_controller():
    return SymbolController()

@router.get("/{symbol}/annual/{year}", response_model= dict[str, str])
def get_symbol_summery(symbol: str = Depends(validate_symbol), year: int = Depends(validate_year), controller: SymbolController = Depends(get_symbol_controller)):

    return controller.get_summary()