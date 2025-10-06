import requests;

url="http://127.0.0.1:5555"

data= {"action": "get-actions", "type": "admin", "token": "MTIzNDU2"} #json data

response=requests.post(url=url,json=data)
print(response.text) # get-users