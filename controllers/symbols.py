from repositories.symbols import SymboleRepository
from clients.alphavantage import AlphaVantageClient

class SymbolController:

    def __init__(self, repository: SymboleRepository, client: AlphaVantageClient):
        self.__repository = repository
        self.__client = client

    def get_summary(self, symbol: str, year: int):

        data = self.__repository.get_summay_by(symbol, year)

        # client_data = self.__client.fetch_by(symbol, year)

        return data


