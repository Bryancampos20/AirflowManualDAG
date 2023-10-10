from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator


dag_id = 'ad_hoc_sync_job'

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 10, 4),
}

dag = DAG(
    dag_id,
    default_args=default_args,
    schedule_interval=None,  # Set the interval to None to avoid automatic scheduling
)

def sync_data_for_user(user_id):
    # Here you can place the logic to synchronize data for the specific user.
    print(f'Synchronizing data for the user with ID: {user_id}')

start_task = DummyOperator(
    task_id='start',
    dag=dag,
)

# Define a PythonOperator task that will execute the ad hoc job.
sync_data_task = PythonOperator(
    task_id='sync_data',
    python_callable=sync_data_for_user,
    op_args=[1],  # Define the specific user ID as an argument.
    dag=dag,
)

start_task >> sync_data_task
