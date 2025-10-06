import subprocess

path=r"C:\Users\Home\Desktop\BLACKBOX7\secret2.exe"

for i in range(301):
    response=subprocess.run(executable=path,args=[],input=str(i).encode(),capture_output=True)
    print(i)
    response=response.stdout.decode().strip()
    if not response.endswith("Wrong checksum!"):
        print(f"SUCCESS! Input number: {i}")
        print(f"Response: {response}")
        break
