
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'Nishchay Linge Gowda',
    'start_date': datetime(2025, 11, 3),
}

dag = DAG(
    'cloud_composer_tutorial_v2',
    default_args=default_args,
    description='DAG with different task outputs',
    schedule_interval=None,  # Manual trigger
)

bash_info_task = BashOperator(
    task_id='show_system_info',
    bash_command='echo "Current Date and Time:" && date && echo "Current Directory:" && pwd',
    dag=dag,
)

def days_until_new_year():
    today = datetime.now()
    new_year = datetime(today.year + 1, 1, 1)
    delta = new_year - today
    print(f"There are {delta.days} days and {delta.seconds // 3600} hours left until New Year {new_year.year}!")

calculate_days_task = PythonOperator(
    task_id='calculate_days_until_new_year',
    python_callable=days_until_new_year,
    dag=dag,
)

# Task dependencies
bash_info_task >> calculate_days_task
