from datetime import timedelta
import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'football_news',
    default_args=default_args,
    description='Football News Data Pipeline',
    schedule_interval="*/2 * * * *",
    catchup=False
)

t1 = BashOperator(
    task_id='scrape',
    depends_on_past=True,
    bash_command='python /usr/local/airflow/dags/scraper/crawl.py italian /usr/local/airflow/data',
    dag=dag,
)

'''t2 = BashOperator(
    task_id='upload',
    depends_on_past=True,
    bash_command='python dags/scraper/upload.py',
    dag=dag,
)

t1 >> t2'''
t1
