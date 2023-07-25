from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args={
    "owner":"manohar",
    "retries":5,
    "retry_delay": timedelta(minutes=2)
}

def greeting():
    a=1+3
    print("Hello world!")
    return a

def addition():
    c=3+2
    print("addition of two numbers",c)
    return c

with DAG(dag_id='assignment_question_1',
         default_args=default_args,
         description='This is our first dag we write',
         start_date=datetime(2023, 7, 25),
         schedule_interval="@daily",
         catchup=False) as dag:
    task1 = PythonOperator(
        task_id="first_one",
        python_callable=greeting
    )
    task2=PythonOperator(
        task_id="second_one",
        python_callable=addition
    )
    task1>>task2

