import hashlib

def md5(input_string):
    return hashlib.md5(input_string.encode('utf-8')).hexdigest()

def sha1(input_string):
    return hashlib.sha1(input_string.encode('utf-8')).hexdigest()

def sha256(input_string):
    return hashlib.sha256(input_string.encode('utf-8')).hexdigest()

target_hashes = [
    {"name": "MD5", "hash_func": md5, "target": "3cc6520a6890b92fb55a6b3d657fd1f6"},
    {"name": "SHA1", "hash_func": sha1, "target": "7c4a8d09ca3762af61e59520943dc26494f8941b"},
    {"name": "SHA256", "hash_func": sha256, "target": "96cae35ce8a9b0244178bf28e4966c2ce1b8385723a96a6b838858cdd6ca0a1e"}
]

found_any_password = False
for num in range(1000000):
    x = str(num).zfill(6) # Generates strings from "000000" to "999999"
    
    for target_info in target_hashes:
        hash_name = target_info["name"]
        hash_func = target_info["hash_func"]
        target_hash_value = target_info["target"]

        if hash_func(x) == target_hash_value:
            print(f"Password found for {hash_name}: {x}")
            found_any_password = True
            break # Break from inner loop (found password for this hash type)
    
if not found_any_password:
    print("No password found within the range for any target hash.")

#Output:
# Password found for MD5: 111158
# Password found for SHA256: 123123
# Password found for SHA1: 123456
# Output is different because the target hashes are different.
