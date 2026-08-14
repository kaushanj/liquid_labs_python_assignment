from repositories.symbols import SymbolRepository
from clients.alphavantage import AlphaVantageClient

from core.exception import NotFoundException

class SymbolController:

    def __init__(self, repository: SymbolRepository, client: AlphaVantageClient):
        self.__repository = repository
        self.__client = client

    def get_summary(self, symbol: str, year: int):

        data = self.__repository.get_summary_by(symbol, year)

        if data is None:
            client_data = self.__client.fetch_by(symbol, year)
            if not client_data:
                raise NotFoundException("No data found for this symbol or year.")

            self.__repository.save_data(client_data)
            data = self.__repository.get_summary_by(symbol, year)

            if data is None:
                raise NotFoundException("No data found for this symbol or year.")

        return data

