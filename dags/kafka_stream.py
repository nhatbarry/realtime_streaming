from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

# default_args = {
#     'owner': 'nhat',
#     'start_date': datetime('2025, 3, 20, 24, 00')
# }

def get_data():
    import requests
    import json
    
    response = requests.get('https://randomuser.me/api/')
    response = response.json()
    return response['results'][0]

def format_data(response):
    data = {}
    data['name'] = f"{response['name']['first']} {response['name']['last']}"
    data['gender'] = response['gender']
    data['age'] = response['dob']['age']
    data['dob'] = response['dob']['date']
    data['username'] = response['login']['username']
    data['password'] = response['login']['password']
    data['address'] = f"{response['location']['street']['number']} {response['location']['street']['name']}, {response['location']['city']}, {response['location']['state']}, {response['location']['country']}"
    data['email'] = response['email']
    data['phone'] = response['phone']
    data['picture'] = response['picture']['medium']
    
    return data

def stream_data():
    res = get_data()
    print(format_data(res))

# with DAG('user_automation',
#             default_args=default_args,
#             schedule_interval='@daily',
#             catchup=False) as dag:
#     streaming_task = PythonOperator(
#         task_id = 'stream_data_from_api'
#         python_callable=stream_data
#     )
    
stream_data()