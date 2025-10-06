import base64
#{"users":[{"date registered":"XX/XX/2019","token":"Y3liZXI=","username":"admin"}]}
token=base64.b64decode("Y3liZXI=").decode()
print(token) #cyber