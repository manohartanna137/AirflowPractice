from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 7, 25),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def add():
    print("please provide proper input")
with DAG(dag_id='assignment_question_4',
         default_args=default_args,
         description='This is our first dag we write using trigger dag run operator',
         start_date=datetime(2023, 7, 25),
         schedule_interval="@daily",
         catchup=False) as dag:


        trigger = TriggerDagRunOperator(
            task_id="test_trigger_dagrun",
            trigger_dag_id="example_trigger_target_dag",
            conf={"message": "Hello World"},
        )