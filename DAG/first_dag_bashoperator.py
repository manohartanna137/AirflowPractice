from datetime import datetime,timedelta
from airflow import DAG

from airflow.operators.bash import BashOperator

default_args={"owner": "manohar",
              "retries":5,
              "retry_delay":timedelta(minutes=2)}


with DAG(dag_id='our_first_dag',
    default_args=default_args,
    description='This is our first dag we write',
    start_date=datetime(2023,7,21),
    schedule_interval='@daily'
    ) as dag:
    task1 =BashOperator(task_id="first_task",
                       bash_command="hello this is the first task"
                        )
    task1