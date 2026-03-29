import os
import sqlite3
import requests
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "weather_data.db")

API_URL = "https://api.open-meteo.com/v1/forecast"
LATITUDE = 6.9271
LONGITUDE = 79.8612
CITY = "Colombo"


def get_weather_data():
    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
    }

    response = requests.get(API_URL, params=params, timeout=30)
    response.raise_for_status()

    data = response.json()
    current = data.get("current", {})

    weather_record = {
        "extraction_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "city": CITY,
        "temperature": current.get("temperature_2m"),
        "humidity": current.get("relative_humidity_2m"),
        "wind_speed": current.get("wind_speed_10m"),
        "description": "Current weather data"
    }

    return weather_record


def save_to_database(record):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO weather_data (
            extraction_time,
            city,
            temperature,
            humidity,
            wind_speed,
            description
        ) VALUES (?, ?, ?, ?, ?, ?)
    """, (
        record["extraction_time"],
        record["city"],
        record["temperature"],
        record["humidity"],
        record["wind_speed"],
        record["description"]
    ))

    conn.commit()
    conn.close()


def main():
    try:
        weather_record = get_weather_data()
        save_to_database(weather_record)
        print("Weather data extracted and saved successfully.")
        print(weather_record)
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()