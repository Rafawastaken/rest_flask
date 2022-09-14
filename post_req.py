# Script to test post request on server api
import requests

TARGET_IP = "http://127.0.0.1:5000/"

data_test = {
    "nome":"video 1",
    "likes": 45,
    "views":1000
}

resp = requests.put(
    TARGET_IP + "video/1", data_test
)

print(resp.json())