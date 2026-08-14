from repositories.symbols import Symbolerepository

class SymbolController:

    def __init__(self, repository: Symbolerepository):
        self.__repository = repository

    def get_summary(self, symbol: str, year: int):

        return self.__repository.get_summay_by(symbol, year)
