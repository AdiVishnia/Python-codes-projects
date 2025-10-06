import subprocess

path=r"C:\Users\Home\Desktop\BLACKBOX2\blackbox2\stage2.exe"
first_6_digits_of_phone_number="052538"

for i in range(4970,10000):
	i=str(i).zfill(4)
	phone_num=first_6_digits_of_phone_number+i
	print(phone_num)
	try:
		result=subprocess.run(
			executable=path,
			args=[],
			input=phone_num.encode(),
			capture_output=True
		)
		output=result.stdout.decode(errors="ignore").strip()
		if not output.endswith("number:"):
			print("Found the number:",phone_num)
			break
	except FileNotFoundError:
		print("Executable not found:", path)
		break