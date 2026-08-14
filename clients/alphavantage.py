import os
import requests
from datetime import datetime 
from fastapi import HTTPException, status

from core.constants import (
    ALPHA_VANTAGE_FUNCTION_NAME,
    ALPHA_VANTAGE_URL
)


class AlphaVantageClient:

    def fetch_by(self, symbol: str, year: int):

        data = self.__make_call(symbol)
        monthly_data = data.get("Monthly Time Series")

        if not monthly_data:
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE , detail="Unexpected error occur. try again later.")

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
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE , detail="API key is missing.")

        try:
            response = requests.get(ALPHA_VANTAGE_URL, 
                                    params={
                "function": ALPHA_VANTAGE_FUNCTION_NAME,
                "symbol": symbol, 
                "apikey": API_KEY
            },
            timeout=10)

            response.raise_for_status()
        except requests.Timeout:
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE , detail="Market data provider timed out.")


        data = response.json()

        if "Information" in data:
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE , detail="Daily limit reach.")
        
        if "Error Message" in data:
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE , detail="Unexpected error occor. try again later.")

        return data
        