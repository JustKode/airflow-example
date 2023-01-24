from datetime import datetime, timedelta
from textwrap import dedent

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "justkode",
}

with DAG(
    "pow_sum_dag",
    default_args=default_args,
    description="Pow and Sum DAG",
    schedule_interval=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['practice']
) as dag:

    def extract(**kwargs):
        ti = kwargs['ti']
        data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ti.xcom_push('data_list', data_list)
    
    def transform(**kwargs):
        ti = kwargs['ti']
        extract_data_list = ti.xcom_pull(task_ids='extract', key='data_list')
        result = 0

        for elem in extract_data_list:
            result += elem ** 2
        
        ti.xcom_push('result', result)
    
    def load(**kwargs):
        ti = kwargs['ti']
        result = ti.xcom_pull(task_ids='transform', key='result')
        print("Result: " + str(result))
    
    extract_task = PythonOperator(
        task_id='extract',
        python_callable=extract
    )

    transform_task = PythonOperator(
        task_id='transform',
        python_callable=transform
    )

    load_task = PythonOperator(
        task_id='load',
        python_callable=load
    )
    
    extract_task >> transform_task >> load_task