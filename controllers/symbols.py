from repositories.symbols import Symbolerepository
from clients.alphavantage import AlphaVantageClient

class SymbolController:

    def __init__(self, repository: Symbolerepository, client: AlphaVantageClient):
        self.__repository = repository
        self.__client = client

    def get_summary(self, symbol: str, year: int):

        row_data = self.__client.fetch_by(symbol, year)

        self.__repository.save_data(data=row_data)

        return self.__repository.get_summay_by(symbol, year)


