from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

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
    task2= BashOperator(task_id="Second_task",
                        bash_command="echo hey i am executing the second task")
    task3 = BashOperator(task_id="third_task",
                         bash_command="echo this is the third task and it is dependent on task1")
    task1>>task2,
    task1>>task3