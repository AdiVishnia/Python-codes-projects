#תרגיל מחשבון
num1=input("Enter num1: ")
op=input("Enter an operator: + - / *:") 
num2=input("Enter num2: ")
if(op=="+"):
    print(int(num1)+int(num2))
if(op=="-"):
    print(int(num1)-int(num2))
if(op=="/"):
    if(int(num2)==0):
        print("Error")
    else:
        print(int(num1)/int(num2))
if(op=="*"):
    print(int(num1)*int(num2))