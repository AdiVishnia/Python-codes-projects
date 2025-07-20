my_list=[12,7,8,23,55]
my_list.append(101)
my_list.append(3)
my_tuple=tuple(my_list)
print(len(my_tuple))
if 99 in my_tuple:
    print("Yes")
else:
    print("No")