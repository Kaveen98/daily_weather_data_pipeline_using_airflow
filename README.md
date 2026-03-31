# Daily Weather Data Pipeline Using Airflow

---

## Project Overview
This project is a coursework assignment for building an automated data pipeline using Apache Airflow.

The pipeline:
- extracts daily weather data from a public API
- stores the data in a relational database (SQLite)
- schedules the workflow using Apache Airflow
- generates visual insights using Jupyter Notebook

---

## Tools and Technologies
- Apache Airflow
- Docker and Docker Compose
- Python
- SQLite
- Jupyter Notebook
- Open-Meteo Weather API

---

## Project Structure
```text
daily_weather_data_pipeline_using_airflow/
├── dags/
│   └── weather_pipeline_dag.py
├── data/
│   └── weather_data.db
├── logs/
├── notebooks/
│   └── weather_analysis.ipynb
├── plugins/
├── screenshots/
│   ├── airflow_ui.png
│   ├── dag_run_success.png
│   ├── database_records.png
│   ├── extract_weather_log.png
│   └── visualization_output.png
├── scripts/
│   ├── extract_weather.py
│   └── init_db.py
├── .gitignore
├── docker-compose.yaml
├── README.md
└── requirements.txt
```

---

## Workflow

1. Airflow triggers the DAG
2. The database is initialized if needed
3. Weather data is fetched from the API
4. The data is stored in SQLite
5. Jupyter Notebook reads the stored data
6. Charts are generated for analysis

---

## Database Fields

The `weather_data` table stores:
- `id`
- `extraction_time`
- `city`
- `temperature`
- `humidity`
- `wind_speed`
- `description`

---

## How to Run the Project

### 1. Create and activate the virtual environment
```
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Install Python packages
```
pip install -r requirements.txt
```

### 3. Initialize the SQLite database
```
python scripts\init_db.py
```

### 4. Test the extraction script
```
python scripts\extract_weather.py
```

### 5. Start Airflow with Docker
```
docker compose up -d
```

### 6. Open Airflow UI
##### Open:
```
http://localhost:8080
```

### 7. Airflow login
Use the admin account created/reset during setup.
Example local credentials:
- Username: admin
- Password: admin

### 8. Trigger the DAG
##### In Airflow:
- enable daily_weather_pipeline
- trigger the DAG manually
- inspect Graph view and Logs

### 9. Run the notebook
##### Open:
```
notebooks/weather_analysis.ipynb
```
Run all cells to generate visualizations.

---

### Output:
##### This project produces:
- an automated Airflow DAG run
- stored weather records in SQLite
- time-series visualizations in Jupyter Notebook
- screenshots for coursework evidence

---

### Screenshots Included:
- Airflow UI
- Successful DAG run
- Database records
- Task log output
- Visualization output

---

### Project Goal:

To build a local end-to-end data pipeline that runs once per day, stores structured weather data, and produces simple visual analytics.

---

