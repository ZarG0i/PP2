import psycopg2
from config import DATABASE_CONFIG

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(**DATABASE_CONFIG)
        self.create_tables()
    
    def create_tables(self):
        cur = self.conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS players (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL
            )
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS game_sessions (
                id SERIAL PRIMARY KEY,
                player_id INTEGER REFERENCES players(id),
                score INTEGER NOT NULL,
                level_reached INTEGER NOT NULL,
                played_at TIMESTAMP DEFAULT NOW()
            )
        """)
        self.conn.commit()
        cur.close()
    
    def create_player(self)