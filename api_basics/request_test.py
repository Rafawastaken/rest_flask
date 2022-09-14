# Script to test post request on server api
import requests
import random

TARGET_IP = "http://127.0.0.1:5000/"


for x in range(10):
    rand = random.randint(100, 999)
    rand_2 = random.randint(100, 999)
    rand_3 = random.randint(100, 999)

    data_test = {
        "nome":f"video {rand}",
        "likes": rand_2,
        "views":rand_3
    }

    put_req = requests.put(TARGET_IP + f"video/{x}", data_test)
    print(f"PUT: {put_req.json()}")

# Update video
patch_req = requests.patch(TARGET_IP + f"video/1", {"nome":"Video Atualizado22"})
print(patch_req.json())

get_req = requests.get(TARGET_IP + f"video/1")
print(get_req.json())

