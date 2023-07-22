from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
default_args = {
    "owner": "manohar",
    "retries": 5,
    "retry_delay": timedelta(minutes=2)
}
def greeting():
    print("Hello this is my first task")
def addition():
    print("addition of two numbers",10+20)

with DAG(dag_id='our_first_dag1',
         default_args=default_args,
         description='This is our first dag we write',
         start_date=datetime(2023, 7, 21),
         schedule_interval="@daily",
         catchup=False) as dag:
    task1 = PythonOperator(
        task_id="first_task",
        python_callable=greeting
    )
    task2=PythonOperator(
        task_id="second_task",
        python_callable=addition
    )
    task1>>task2
