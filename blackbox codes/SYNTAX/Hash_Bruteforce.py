import hashlib
hashed_text="e10adc3949ba59abbe56e057f20f883e" #123456
def MD5(hash): #32 תווים
    return hashlib.md5(hash.encode()).hexdigest()
def SHA1(hash): #40 תווים   
    return hashlib.sha1(hash.encode()).hexdigest()
def SHA256(hash): #64 תווים 
    return hashlib.sha256(hash.encode()).hexdigest()

for i in range(1000000):
    hash=str(i) #חייב להיות string
    if(MD5(hash)==hashed_text):
        print(hash)
        break