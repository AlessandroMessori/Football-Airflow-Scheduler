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
    'email': ['messori.alessandro.98@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'football_news',
    default_args=default_args,
    description='Football News Data Pipeline',
    schedule_interval="0 20 * * *",
    catchup=False
)

t1 = BashOperator(
    task_id='scrape',
    bash_command='python /usr/local/airflow/dags/scraper/crawl.py',
    dag=dag,
)

t2 = BashOperator(
    task_id='upload_raw',
    depends_on_past=False,
    bash_command='python /usr/local/airflow/dags/utils/main.py football-news data',
    dag=dag,
)

t3 = BashOperator(
    task_id='count',
    depends_on_past=False,
    bash_command='python /usr/local/airflow/dags/analytics/main.py ',
    dag=dag,
)

t4 = BashOperator(
    task_id='upload_counters',
    depends_on_past=False,
    bash_command='python /usr/local/airflow/dags/utils/main.py football-counters counters',
    dag=dag,
)

t1 >> t2 >> t3 >> t4
