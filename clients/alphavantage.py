import os
import requests
from datetime import datetime 

from core.exception import ConfigException, ProviderException

from core.constants import (
    ALPHA_VANTAGE_TIME_SERIES_MONTHLY,
    ALPHA_VANTAGE_URL
)


class AlphaVantageClient:

    def fetch_by(self, symbol: str, year: int):
        """ fetch raw stock data from monthly time series """

        data = self.__make_call(symbol)
        monthly_data = data.get("Monthly Time Series")

        if not monthly_data:
            raise ProviderException("Unexpected error occurred. try again later.")

        rows = []
        for date, value in monthly_data.items():
            stock_year = datetime.strptime(date, "%Y-%m-%d").year

            if stock_year != year:
                continue

            rows.append((
                symbol.upper(), 
                date, stock_year, 
                float(value["2. high"]),
                float(value["3. low"]),
                float(value["5. volume"])
            ))

        return rows

    def __make_call(self, symbol: str):
        """ Make api call """
        API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
        
        if not API_KEY:
            raise ConfigException("API key is missing.")

        try:
            response = requests.get(ALPHA_VANTAGE_URL, 
                                    params={
                "function": ALPHA_VANTAGE_TIME_SERIES_MONTHLY,
                "symbol": symbol, 
                "apikey": API_KEY
            },
            timeout=5)

            response.raise_for_status()
        except requests.RequestException:
            raise ProviderException("Market data unavailable.")


        data = response.json()

        if "Information" in data:
            raise ProviderException("Daily limit reach.")
        
        if "Error Message" in data:
            raise ProviderException("Unexpected error occurred. try again later.")

        return data
        