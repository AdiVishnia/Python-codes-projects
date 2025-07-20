# תרגיל 1
def get_value(dictionary,key):
    if key in dictionary.keys():
        print("The key: "+key)
    else:
        print("Erorr!")

my_dict={
    "Name":"Shimi",
    "Age": 31,
    "City":"Tel-Aviv"
}
#get_value(my_dict,"City")

# תרגיל 2
def union_sets(set1,set2):
    return set1.union(set2)
set1={1,2,3}
set2={3,4,5}
print(union_sets(set1,set2))

# תרגיל 3
def count_elements_in_tuples(list1):
    my_dict={}
    for i in range(len(list1)):
        my_tuple=tuple(list1[i])
        for j in range(len(my_tuple)):
            if my_tuple[j] in my_dict.keys():
                my_dict[my_tuple[j]]+=1
            else:
                my_dict[my_tuple[j]]=1
    return my_dict

list1=[('a','b'),('a','c'),('d','b'),('e','f'),('a','b')]
print(count_elements_in_tuples(list1))