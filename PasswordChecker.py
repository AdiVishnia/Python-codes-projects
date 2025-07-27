password=input("Enter Password:") #קבלת סיסמא מהשתמש
count=0 # איתחול הניקוד ל0
#אורך הסיסמא
length=len(password)
if length>=8 and length<=11: 
    count+=1
if length>=12:
    count+=2
#מורכבות
if any(char.islower() for char in password):
    count+=1
if any(char.isupper() for char in password):
    count+=1
if any(char.isdigit() for char in password):
    count+=1
if any(char in "!@#$%^&*()_+=-" for char in password):
    count+=1

#מילים נפוצות
common_words_list=["admin","123456","password"]
for i in range(len(common_words_list)):
    if common_words_list[i] in password:
        count -=2


#דירוג סופי לפי ניקוד כולל
if count<=0:
    print("Weak password!")
if count>=1 and count <=3:
    print("Medium password!")
if count>=4:
    print("Strong password!")
