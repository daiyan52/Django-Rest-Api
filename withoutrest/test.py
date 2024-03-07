import requests

BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'testapp/apijsoncbv1/'
resp = requests.delete(BASE_URL + END_POINT)

if resp.status_code == 200:
    data = resp.json()
    print(data)
else:
    print("Failed to fetch data:", resp.status_code)
