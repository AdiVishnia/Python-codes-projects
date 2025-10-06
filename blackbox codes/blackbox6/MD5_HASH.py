import hashlib

password=hashlib.md5("helloworld!".encode()).hexdigest()
print(password)