import  hashlib

secret="6688795677c1c8f2d3cd14b710f60153"
first_6_digits_of_phone_number="052538"  #052538 XXXX

def MD5(pnumber):
    return hashlib.md5(pnumber.encode()).hexdigest()

for i in range(10000):
	i=str(i).zfill(4)
    phone_number=first_6_digits_of_phone_number+i
    if(MD5(phone_number)==secret):
        print("correct phone number: {}".format(phone_number))
        break