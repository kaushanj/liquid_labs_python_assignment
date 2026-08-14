import sqlite3
from pathlib import Path

DB_PATH = Path("market.db")



def create_market_data_table():

    query = """
CREATE TABLE IF NOT EXISTS market_data (
id INTEGER PRIMARY KEY AUTOINCREMENT,
symbol TEXT NOT NULL,
date TEXT NOT NULL,
year INTEGER NOT NULL,
low REAL NOT NULL,
high REAL NOT NULL,
volume INTEGER NOT NULL, 
UNIQUE (symbol, date)
)

"""

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(query)
        conn.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_market_data_symbol_year ON
            market_data(symbol,year)
            """
        )
        conn.commit()


def get_db():
    conn = sqlite3.connect(DB_PATH)
    
    try:
        yield conn
    finally:
        conn.close()