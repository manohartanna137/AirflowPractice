from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args={
    "owner":"manohar",
    "retries": 5,
    "retry_interval":timedelta(minutes=2)
}

def wish(ti):
    name=ti.xcoms_pull(task_ids="name_of_person")
    print(f"my name is {name}")
def name_of_person():
    a='manohar'
    return a

with DAG(dag_id = 'xcomdag',
         default_args=default_args,
         description= 'Trying this dag using xcom' ,
         start_date = datetime(2023, 7, 26),
         schedule="@daily",
    catchup=True
         ) as dag:

    task1=PythonOperator(
        task_id="wish",
        python_callable=wish
    )
    task2=PythonOperator(
        task_id="name_of_person",
        python_callable=name_of_person
    )

    task2>>task1




