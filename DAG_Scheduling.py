# Airflow Mini-Project

# Task:
# - To extract online stock market data and deliver analytical
# results.

# Think:
# - We are trying to download stock data from both Tesla and Apple for upstream analysis.

# Helpful Link:
# https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html

# Import Packages
import sys
import logging
import yfinance as yf
import pandas as pd
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import date, timedelta, datetime


# Use function for creating operators t1 and t2
def download_file(stock_ticker):
    """
    This function will take in a stock ticker as a string and download data
    from the 'Yahoo Finance' module based an given start and end date.

    We will use this function as arguments for both of the PythonOperators
    in task1 and task2.

    :param stock_ticker: The stock ticker in form of string.
    :return: No output. Simple function call will output data into a CSV file.
    """
    start_date = today
    end_date = start_date + timedelta(days=1)
    df = yf.download(stock_ticker, start=start_date, end=end_date, interval='1m')
    df.to_csv(stock_ticker + '_data.csv', header=True)


# Create function for task 5
def run_custom_query():
    """
    This function will mainly be used to read the data stored inside the temporary directory
    created from the BashOperator of task 1. We use pandas to read each csv file
    sorted by "date time" in ascending order. Then, we return custom_query
    (find middle value of high and low for each stock).

    :return: Custom query of data (middle value between high and low) for Apple and Tesla stock stored inside list object.
    """
    apple_df = pd.read_csv("/tmp/data/" + str(today) + "/AAPL_data.csv", header=0)
    tesla_df = pd.read_csv("/tmp/data/" + str(today) + "/TSLA_data.csv", header=0)
    custom_query = [(apple_df['High'][0] + apple_df['Low'][0]) / 2, (tesla_df['High'][0] + tesla_df['Low'][0]) / 2]
    print(f"Custom query: {custom_query}")
    return custom_query


# Obtain today's date
today = date.today()

# Default arguments for DAG creation
default_args = {
    'owner': 'admin2',
    'start_date': datetime.now() - timedelta(days=1)  # ,
    # 'depends_on_past': False,
    # 'email_on_failure': False,
    # 'retries': 2,
    # 'retry_delay': timedelta(minutes=5)
}

# Cron expression example:
# 5 4 * * *
# (Order: minute, hour, day (of month), month, day (of week)

# * - any value
# + value list separator
# - range of values
# / step values

# The following can be used for schedule_interval parameter in non-standard format:
# @yearly
# @annually
# @monthly
# @weekly
# @yearly

# Use DAG context manager

# - For schedule_interval, we want to set minute to *,
# hour to 18 because of "PM", day of month to *, month to *
# and day of week to 1-5 (M-f).


with DAG(dag_id='marketvol',
         default_args=default_args,
         description='DAG to extract Apple and Tesla data '
                     'and run custom query',
                # schedule_interval="* 18 * * 1-5"
                # Change to --> @hourly or '* * * * *' --> for every minute.
                schedule_interval='0 16 * * 1-6'
         ) as dag:

    # Create BashOperator to initialized temporary directory for data download (t0)
    t0 = BashOperator(
        task_id="t0",
        bash_command="mkdir -p /tmp/data/" + str(today)
    )

    t1 = PythonOperator(
        task_id="t1",
        python_callable=download_file,
        op_kwargs={'stock_ticker': 'TSLA'}
    )

    t2 = PythonOperator(
        task_id="t2",
        python_callable=download_file,
        op_kwargs={'stock_ticker': 'AAPL'}
    )

    t3 = BashOperator(
        task_id='t3',
        bash_command='mv /opt/airflow/TSLA_data.csv /tmp/data/' + str(today) + "/"
    )

    t4 = BashOperator(
        task_id='t4',
        bash_command='mv /opt/airflow/AAPL_data.csv /tmp/data/' + str(today) + "/"
    )

    t5 = PythonOperator(
        task_id="t5",
        python_callable=run_custom_query
    )


# Set job dependencies

t0 >> t1 >> t3 >> t5
t0 >> t2 >> t4

# Log file is present in DAG_Scheduling.py.log.
