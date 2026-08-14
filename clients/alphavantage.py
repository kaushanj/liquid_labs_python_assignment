import os
import requests
from datetime import datetime 

from core.constants import (
    ALPHA_VANTAGE_FUNCTION_NAME,
    ALPHA_VANTAGE_URL
)


class AlphaVantageClient:

    def fetch_by(self, symbol: str, year: int):

        API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

        response = requests.get(ALPHA_VANTAGE_URL, 
                                    params={
                "function": ALPHA_VANTAGE_FUNCTION_NAME,
                "symbol": symbol, 
                "apikey": API_KEY
            },
            timeout=10)

        response.raise_for_status()

        data = response.json()

        monthly_data = data.get("Monthly Time Series")

        rows = []
        for date, value in monthly_data.items():
            stock_year =  datetime.strptime(date, "%Y-%m-%d").year

            rows.append((
                symbol.upper(), 
                date, stock_year, 
                float(value["2. high"]),
                float(value["3. low"]),
                float(value["5. volume"])
            ))

        return rows