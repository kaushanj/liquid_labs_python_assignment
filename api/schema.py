from fastapi import HTTPException, status
def validate_symbol(symbol: str) -> str:
    """ validate symbol"""
    if not symbol.isalpha():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Symbol.")

    return symbol

def validate_year(year: int) -> int:
    """ validate year"""

    if year < 1000 or year > 9999:

        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Must be a valid year.")

    return year