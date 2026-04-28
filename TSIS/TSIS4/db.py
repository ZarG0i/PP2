import psycopg2
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT


def get_connection():
    try:
        return psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
    except Exception as e:
        print("DB connection error:", e)
        return None


def create_tables():
    conn = get_connection()
    if conn is None:
        return

    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS players (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS game_sessions (
        id SERIAL PRIMARY KEY,
        player_id INTEGER REFERENCES players(id),
        score INTEGER NOT NULL,
        level_reached INTEGER NOT NULL,
        played_at TIMESTAMP DEFAULT NOW()
    );
    """)

    conn.commit()
    cur.close()
    conn.close()


def get_or_create_player(username):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id FROM players WHERE username = %s", (username,))
    result = cur.fetchone()

    if result:
        player_id = result[0]
    else:
        cur.execute("INSERT INTO players(username) VALUES (%s) RETURNING id", (username,))
        player_id = cur.fetchone()[0]
        conn.commit()

    cur.close()
    conn.close()

    return player_id


def save_game(username, score, level):
    conn = get_connection()
    cur = conn.cursor()

    player_id = get_or_create_player(username)

    cur.execute("""
    INSERT INTO game_sessions(player_id, score, level_reached)
    VALUES (%s, %s, %s)
    """, (player_id, score, level))

    conn.commit()
    cur.close()
    conn.close()


def get_leaderboard():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT p.username, g.score, g.level_reached, g.played_at
    FROM game_sessions g
    JOIN players p ON g.player_id = p.id
    ORDER BY g.score DESC
    LIMIT 10
    """)

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows


def get_personal_best(username):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT MAX(g.score)
    FROM game_sessions g
    JOIN players p ON g.player_id = p.id
    WHERE p.username = %s
    """, (username,))

    result = cur.fetchone()

    cur.close()
    conn.close()

    return result[0] if result[0] else 0