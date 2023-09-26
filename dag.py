# import the libraries

from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago

#defining DAG arguments

# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'LongNH4',
    'start_date': days_ago(0),
    'email': ['ramesh@somemail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# defining the DAG

# define the DAG
dag = DAG(
    'DataMartDetailVnEwt',
    default_args=default_args,
    description='Job Ingest DataMart Detail Vnpayewt',
    schedule_interval=timedelta(days=1),
)

# define the tasks

# define the first task

submit = BashOperator(
    task_id='submit',
    bash_command='bash /home/longnh4/bin/DataMartDetailVnEwt.sh',
    dag=dag,
)

# task pipeline
submit
