from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args={
    "owner":"manohar",
    "retries":5,
    "retry_delay": timedelta(minutes=2)
}


with DAG(dag_id='assignment_question_2',
         default_args=default_args,
         description='This is our first dag we write',
         start_date=datetime(2023, 7, 25),
         schedule_interval="@daily",
         catchup=False) as dag:
   task1=BashOperator(
        task_id="task_1",
       bash_command="echo 'Hello, this is the  task! related to assignment'"
   )
   task2=BashOperator(
       task_id="task_2",
       bash_command="echo 'Execute my second task'"
   )

task2>>task1



