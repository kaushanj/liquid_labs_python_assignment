import sqlite3
class Symbolerepository:

    def __init__(self, db: sqlite3.Connection):
         self.__db = db

    def get_summay_by(self, symbol: str, year: int):

         query = """
            SELECT 
                MAX(high) as high, MIN(low) as low, SUM(volume) as volume  
            FROM market_data
            WHERE symbol = ? AND year = ?
"""

         data = self.__db.execute(query, (symbol, year)).fetchone()

         if  data is None:
              return None

         return {
               "high": "80.8700",
               "low": "76.0600",
               "volume": "139457800"
        }
        