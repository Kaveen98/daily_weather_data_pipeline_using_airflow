from datetime import datetime, timedelta
import os
import sys

from airflow import DAG
from airflow.operators.python import PythonOperator

# Add project root to Python path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from scripts.init_db import create_database
from scripts.extract_weather import get_weather_data, save_to_database


def initialize_database():
    create_database()


def extract_and_store_weather():
    weather_record = get_weather_data()
    save_to_database(weather_record)
    print("Weather data saved successfully.")
    print(weather_record)


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="daily_weather_pipeline",
    default_args=default_args,
    description="A daily weather data pipeline using Apache Airflow",
    start_date=datetime(2026, 3, 29),
    schedule_interval="@daily",
    catchup=False,
    tags=["weather", "pipeline", "coursework"],
) as dag:

    init_db_task = PythonOperator(
        task_id="initialize_database",
        python_callable=initialize_database,
    )

    extract_weather_task = PythonOperator(
        task_id="extract_and_store_weather",
        python_callable=extract_and_store_weather,
    )

    init_db_task >> extract_weather_task