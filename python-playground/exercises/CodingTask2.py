#תרגיל 1
def find_longest_word(words_list):
    max=0
    max_word_list=[]
    for i in range(len(words_list)):
        if(len(words_list[i])>max):
            max=len(words_list[i])
    for i in range(len(words_list)):
        if(len(words_list[i])==max):  
            max_word_list.append(words_list[i])      
    return max_word_list
#בדיקה
words_list=['apple','banana','orange','strawbery','pineapple','kiwi']
print(find_longest_word(words_list))

#תרגיל 2
#פעולת עזר
def reverse(text):
    return text[: :-1]
#פעולת עזר
def is_polindrom(string):
    if(string==reverse(string)):
        return True
    return False

def find_palindromes(str_list):
    result=[]
    for i in range(len(str_list)):
        if(is_polindrom(str_list[i])):
            result.append(str_list[i])
    return result

str_list=['radar','apple','level','banana','stats','noon']
print(find_palindromes(str_list))