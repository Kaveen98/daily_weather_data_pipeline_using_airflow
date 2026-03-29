# Daily Weather Data Pipeline Using Airflow

## Project Overview
This project is a coursework assignment for building an automated data pipeline using Apache Airflow.  
The pipeline will extract daily weather data from a public API, store it in a relational database, and generate visual insights using Jupyter Notebook.

## Tools and Technologies
- Apache Airflow
- Docker and Docker Compose
- Python
- SQLite
- Jupyter Notebook
- Public Weather API

## Planned Project Structure
- `dags/` - Airflow DAG files
- `scripts/` - Python scripts for extraction and database setup
- `notebooks/` - Jupyter Notebook for visualization
- `data/` - SQLite database file
- `screenshots/` - Required screenshots for the report

## Project Goal
To build a local end-to-end data pipeline that runs once per day, stores structured weather data, and produces simple visual analytics.