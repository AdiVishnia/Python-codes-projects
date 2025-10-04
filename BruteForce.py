import hashlib

def md5(input_string):
    return hashlib.md5(input_string.encode('utf-8')).hexdigest()

target_hash = "3cc6520a6890b92fb55a6b3d657fd1f6"

for num in range(1000000):  
    x = str(num).zfill(6)  
    if md5(x) == target_hash:
        print(f"passowrd: {x}")
        break
