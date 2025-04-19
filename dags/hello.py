from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def print_hello():
    return "Hello World"

dag = DAG("hello_world_helmi", description="Hello World with Python Operator",
          schedule_interval='@daily',
          start_date=datetime(2025,4,19),
          catchup=False,
          tags=["Helmi", "example","hello_world"])

task_hello = PythonOperator(
    task_id ='print_hello',
    python_callable=print_hello,
    dag=dag
)

task_hello