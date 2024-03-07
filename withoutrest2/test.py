import requests

BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'testapp/api/'

def get_resorce(id):
    resp = requests.get(BASE_URL + END_POINT + str(id))
    print(resp.status_code)
    print(resp.json())

get_resorce(2)