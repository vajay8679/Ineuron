#import required packages
import airflow
from airflow import DAG
from airflow.operators.hive_operator import HiveOperator
from airflow.utils.dates import days_ago

#Hive task
dag_hive = DAG(dag_id = "hive_script2",
  schedule_interval = '0 0 * * *',
  start_date = airflow.utils.dates.days_ago(1))

hql_query = """use default;
create table if not exists airflow_hive(id int, name string);
insert into airflow_hive values(1, "bigdata");"""

hive_task = HiveOperator(hql = hql_query, task_id = "hive_script_task2", hive_cli_conn_id = "hive_local", dag = dag_hive)

hive_task

if __name__ == '__main__':
  dag_hive.cli()
