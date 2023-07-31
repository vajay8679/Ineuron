import airflow
from airflow.models import DAG
from airflow.providers.apache.hive.operators.hive import HiveOperator
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator

dag_hive = DAG(dag_id = "hive_script",
          schedule_interval = '00 1 * * *',
            start_date = airflow.utils.dates.days_ago(1))

hql_query = """create database if not exists mydb;
CREATE TABLE IF NOT EXISTS mydb.test_af(
`test` int);
insert into mydb.test_af values (2);
"""
run_this = BashOperator(
            task_id='run_after_loop',
                bash_command='echo `whoami`',
                )

hive_task = HiveOperator(hql = hql_query,
          task_id = "hive_script_task",
            hive_cli_conn_id = "hive_local",
              dag = dag_hive
              )

run_this >> hive_task

if __name__ == '__main__ ':
      dag_hive.cli()