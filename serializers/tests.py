import requests
import json
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'

def get_resourec(id):
    resp = requests.get(BASE_URL + END_POINT + str(id))
    if resp.status_code in range(200,300):
        print(resp.status_code)
        data = resp.json()
        print(data)
    else:
        print("Failed to fetch data:")
get_resourec(3)
print('All')
def get_all():
    resp = requests.get(BASE_URL + END_POINT)
    print(resp.status_code)
    print(resp.json())
get_all()

# def create_resource():
#     new_stu = {
#         'name': 'Anis',
#         'roll': 1,
#         'address': 'Sitamarhi, Bihar',
#     }
#     resp = requests.post(BASE_URL + END_POINT, data=json.dumps(new_stu))
#     print(resp.status_code)
#     print(resp.json())
# create_resource()


# def update_resource(id):
#     print(id)
#     new_stu = {
#         'name' : 'Praveen',
#         'roll': 46,
#         'address': 'Patna, Bihar',
#     }
#     resp = requests.put(BASE_URL + END_POINT + str(id) + '/', data=json.dumps(new_stu))
#     print(resp.status_code)
#     print(resp.json())

# update_resource(3)

def delete_resource(id):
    print(id)
    resp = requests.delete(BASE_URL + END_POINT + str(id) + '/')
    print(resp.status_code)
    print(resp.json())
delete_resource(6)