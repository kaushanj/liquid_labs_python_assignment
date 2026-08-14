from core.exception import ValidationException

def validate_symbol(symbol: str) -> str:
    """ validate symbol"""

    symbol = symbol.strip().upper()
    if not symbol.isalpha() or len(symbol) > 10:
        raise ValidationException("Invalid symbol.")


    return symbol

def validate_year(year: int) -> int:
    """ validate year"""

    if year < 1000 or year > 9999:

        raise ValidationException("Must be a valid year.")

    return year