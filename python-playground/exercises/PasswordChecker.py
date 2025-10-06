password=input("Enter Password:") # Get password from user
count=0 # Initialize score to 0
# Password length
length=len(password)
if length>=8 and length<=11: 
    count+=1
if length>=12:
    count+=2
# Complexity
if any(char.islower() for char in password):
    count+=1
if any(char.isupper() for char in password):
    count+=1
if any(char.isdigit() for char in password):
    count+=1
if any(char in "!@#$%^&*()_+=-" for char in password):
    count+=1

# Common words
common_words_list=["admin","123456","password"]
for i in range(len(common_words_list)):
    if common_words_list[i] in password:
        count -=2


# Final rating based on total score
if count<=0:
    print("Weak password!")
if count>=1 and count <=3:
    print("Medium password!")
if count>=4:
    print("Strong password!")
