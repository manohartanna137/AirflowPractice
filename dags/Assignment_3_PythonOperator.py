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
def divison_of_two(a=10,b=2):
    return a%b

with DAG(dag_id='assignment_question_3',
         default_args=default_args,
         description='This is our first dag we write',
         start_date=datetime(2023, 7, 25),
         schedule_interval="@daily",
         catchup=False) as dag:
    task1 = PythonOperator(
        task_id="first_one_greeting",
        python_callable=greeting
    )
    task2=PythonOperator(
        task_id="second_one_addition",
        python_callable=addition
    )
    task3=PythonOperator(
        task_id="third_one_divison",
        python_callable= divison_of_two
    )
    task1>>task2
    task2>>task3

