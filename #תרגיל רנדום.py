#תרגיל רנדום
import random
secret_number=random.randint(1,100)
while True:
    num=int(input("Enter a number: "))
    if(num==secret_number):
        print("You guessed the right number!")
        break
    if(num<secret_number):
        print("Your num is lower than the secret number")
    if(num>secret_number):
        print("Your num is higher than the secret number")
      