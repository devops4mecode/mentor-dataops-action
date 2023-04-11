from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'me',
    'depends_on_past': False,
    'start_date': datetime(2022, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'my_dag',
    default_args=default_args,
    description='A simple DAG',
    schedule_interval=timedelta(days=1),
)

t1 = BashOperator(
    task_id='task_1',
    bash_command='echo "Task 1"',
    dag=dag,
)

t2 = BashOperator(
    task_id='task_2',
    bash_command='echo "Task 2"',
    dag=dag,
)

t3 = BashOperator(
    task_id='task_3',
    bash_command='echo "Task 3"',
    dag=dag,
)

t1 >> t2 >> t3