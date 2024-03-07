import requests
import json
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'

def get_data(id=None):
    data ={}
    if id is not None:
        data ={
            'id':id
        } 
    resp = requests.get(BASE_URL + END_POINT, data = json.dumps(data))
    print(resp.status_code)
get_data()