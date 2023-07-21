from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import pythonoperator
default_args = {
    "owner": "manohar",
    "retries": 5,
    "retry_delay": timedelta(minutes=2)
}

with DAG(dag_id='our_first_dag',
         default_args=default_args,
         description='This is our first dag we write',
         start_date=datetime(2023, 7, 21),
         schedule_interval="@daily",
         catchup=False) as dag:
    task1 = BashOperator(
        task_id="first_task",
        bash_command="echo 'Hello, this is the first task!'"
    )
    task2 = Pythonoperator