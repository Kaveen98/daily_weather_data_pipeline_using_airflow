import sqlite3
import os

# Build path to the database file inside the data folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "weather_data.db")


def create_database():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            extraction_time TEXT NOT NULL,
            city TEXT NOT NULL,
            temperature REAL,
            humidity INTEGER,
            wind_speed REAL,
            description TEXT
        )
    """)

    conn.commit()
    conn.close()

    print(f"Database initialized successfully at: {DB_PATH}")


if __name__ == "__main__":
    create_database()