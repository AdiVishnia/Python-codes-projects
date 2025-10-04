import hashlib

cryptxt=hashlib.sha1(b"hello")
cryptxt=cryptxt.hexdigest()
print(cryptxt)