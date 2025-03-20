from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

# default_args = {
#     'owner': 'nhat',
#     'start_date': datetime('2025, 3, 20, 24, 00')
# }

def get_data():
    import requests
    
    response = requests.get('https://randomuser.me/api/')
    response = response.json()
    return response['results'][0]

def stream_data():
    import json
    

# with DAG('user_automation',
#             default_args=default_args,
#             schedule_interval='@daily',
#             catchup=False) as dag:
#     streaming_task = PythonOperator(
#         task_id = 'stream_data_from_api'
#         python_callable=stream_data
#     )
    
stream_data()