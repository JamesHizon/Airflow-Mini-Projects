# Airflow Mini Projects

This repository will include both Airflow Mini-Projects from Springboard.

## Airflow Mini Project 1 - DAG Scheduling
In this mini-project, I use Apache Airflow to create a data pipeline to extract online stock market data and deliver analytical results using Yahoo Finance as a data source.

### Prerequisites:
1) Install Airflow: http://airflow.apache.org/docs/stable/installation.html 
Also, install using command: ```pip install apache-airflow```
2) Use Yahoo Finance's Python library: ```pip install yfinance```
3) Install pandas: ```pip install pandas```.

### Update:
I had to use run Airflow on ```Docker```, so I did not end up requiring the previously installed ```apache-airflow```. Thus, refer to ```Command_Line_Execution.txt``` file to see how I executed my Python script.
I instead had to work w/ a provided folder from Springboard mentor to run airflow, where you can email me at jrhizon@ucdavis.edu and I will get back to you as soon as possible.

After completing necessary steps in command line, type ```localhost:8080``` into browser to observe Airflow UI to analyze Airflow DAG information.
