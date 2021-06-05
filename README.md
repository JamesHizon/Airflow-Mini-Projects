# Airflow Mini Projects

This repository will include both Airflow Mini-Projects from Springboard.

## Airflow Mini Project 1 - DAG Scheduling
In this mini-project, I use Apache Airflow to create a data pipeline to extract online stock market data and deliver analytical results using Yahoo Finance as a data source.

### Prerequisites:
1) Install Airflow: http://airflow.apache.org/docs/stable/installation.html 
Also, install using command: ```pip install apache-airflow```
2) Use Yahoo Finance's Python library: ```pip install yfinance```
3) Install pandas: ```pip install pandas```.

### How to execute run DAG:
First, set up airflow database, web server and scheduler. Note that login info may be required (see Airflow document).
```
airflow initdb
airflow webserver
airflow scheduler
```
Then, go to airflow directory. 

```
cd Airflow
cd dags
```

Next, copy Python file into dag folder based on working directory. (Copy and paste full Python file directory vs. what is shown.)

```
cp ~/DAG_Scheduling.py
```

Now, type ```localhost:8080``` into browser to observe Airflow UI to analyze Airflow DAG information.
