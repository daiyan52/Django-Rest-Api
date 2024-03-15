import requests
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'
import time
print('All Data')
def get_data():
    resp = requests.get(BASE_URL + END_POINT)
    print(resp.status_code)
    print(resp.json())
get_data()
print()
time.sleep(2)
print()
def get_data_by_id(id):
    resp = requests.get(BASE_URL + END_POINT + str(id))
    print('Details of id :',id)
    print(resp.status_code)
    print(resp.json())
get_data_by_id(1)