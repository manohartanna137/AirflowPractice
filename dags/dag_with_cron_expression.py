from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "manohar",
    "retries": 5,
    "retry_delay": timedelta(minutes=2)
}

def first_task_function():
    print('Hello, this is the first task!')
def addition_of_two_num():
    print('addition of two numbers is:',10+20)

with DAG(dag_id='python_dag_with_cron_expression',
         default_args=default_args,
         description='This is our first dag we write',
         start_date=datetime(2023, 7, 22),
         schedule_interval="0 0 * * *",
         catchup=False) as dag:

    task1 = PythonOperator(
        task_id="python_first_task",
        python_callable=first_task_function
    )
    task2=PythonOperator(
        task_id="python_second_task",
        python_callable=addition_of_two_num
    )
    task1<<task2
