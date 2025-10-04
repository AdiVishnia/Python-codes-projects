# def modify_list(lst):
#     lst.append(4)
#     lst=[5,6,7]
#     lst.append(8)
#     return lst

# numbers=[1,2,3]
# new=modify_list(numbers)
# print(numbers)  
# print(new)
# x=8
# x=x>>1
# print(x)
# list=[1,2,3]
# x=list.pop()
# print(x)
# def modify_list(lst):
#     lst+=[4,5,6]

# data=[1,2,3]
# modify_list(data)   
# print(data)
# for i in range(1,6,2):
#     print(i)
# text_data="hello\n  world\n  this\n is\n  python "
# lines=text_data.split('\n')
# print(lines[4].strip())
# dict_data={'a':1,'b':2,'c':3,'a':9}
# print(dict_data['a'])
# lst=[10,20,30,40,50]
# print(lst[-3:])
# tuple_data=(10,20,30,40,50)
# tuple_data[-1]=100
# print(tuple_data) 
def mystery_function():
    for i in range(5):    
        yield i
myetry_gen=mystery_function()
for value in myetry_gen:
    print(value)