import sqlite3

class SymbolRepository:

    def __init__(self, db: sqlite3.Connection):
         self.__db = db

    def get_summary_by(self, symbol: str, year: int):
        """ fetch summary data from db """

        query = """
            SELECT 
                MAX(high) as high, MIN(low) as low, SUM(volume) as volume  
            FROM market_data
            WHERE symbol = ? AND year = ?
        """

        data = self.__db.execute(query, (symbol, year)).fetchone()


        if  data is None or data["high"] is None:
            return None

        return {
            "high": str(data["high"]),
            "low": str(data["low"]),
            "volume": str(data["volume"])
        }

    def save_data(self, data: list):

        query = """
        INSERT INTO market_data (symbol, date, year, high, low, volume ) VALUES (
        ?, ?, ?, ?, ?, ?)
        """

        self.__db.executemany(query, data)
        self.__db.commit()
        