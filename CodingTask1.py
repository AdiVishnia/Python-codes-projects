#תרגיל 1
numbers=[3,5,2,8,1,9,4]
max=0
for i in range(len(numbers)):
    if(numbers[i]>max):
        max=numbers[i]
print(max)

#תרגיל 2
def even_list(original_list):
    result = []
    for num in original_list:
        if num % 2 == 0:
            result.append(num)
    return result
original_list=[1,4,5,7,8,10,13]
print(even_list(original_list))

#תרגיל 3
def is_up_list(test_list):
    for i in range(len(test_list)-1):
        if(test_list[i]>test_list[i+1]):
            return False
    return True
test_list=[1,2,3,4,5]
print(is_up_list(test_list))

#תרגיל 4
text="!Hello, world"
print(text[: :-1])

#תרגיל 5
def nikud_letter_count(text):
    count=0
    for i in range(len(text)):
        letter=text[i]
        if(letter in 'aeiou'):
            count+=1
    return count
print(nikud_letter_count("hello"))

#בונוס
# תרגיל 1
def is_prime(num):
    if(num<2):
        return False
    for i in range(2,10):
        if(num%i==0 and i!=num):
            return False
    return True

def prime_numbers(x,y):
    for i in range(x,y+1):
        if(is_prime(i)):
            print(i)

prime_numbers(1,100)

# תרגיל 2
def reverse(text):
    return text[: :-1]
# תרגיל 3
def is_polindrom(string):
    if(string==reverse(string)):
        return True
    return False
print(is_polindrom("ABA")) # True
# תרגיל 4
def longest_word(sentence):
    result = []
    start=0
    max=0
    for i in range(len(sentence)):
        if sentence[i] == " ":
            result.append(sentence[start:i])
            start=i+1
    result.append(sentence[start:len(sentence)])
    for i in range(len(result)):
        if(len(result[i])>max):
            max=len(result[i])
            maxword=result[i]
    return maxword

sentence="Yoni is very good in coding"
print(longest_word(sentence))