class_dictionery={
    "Moshe": 98 ,
    "Adi": 100,
    "Yoni":55,
    "Shai":67
}
class_dictionery["Arad"]=99
class_dictionery["Shai"]=71
print(class_dictionery)
sum=0
for value in class_dictionery.values():
    sum+=value
avg=sum/len(class_dictionery)
print(avg)
class_dictionery.pop("Shai")
print(class_dictionery)
if "Adi" in class_dictionery:
    print("Found")
else:
    print("Not Found")