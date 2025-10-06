import sys
# This program counts the frequency of each word in a text file and prints the top N most common words.
# to run the program, use command line argument to input N value
# Example: python -u "d:\python codes\Word_Frequency_Counter.py" 10
try:
    N=int(sys.argv[1]) #input N from user by using sys.argv
except:
    print("Invalid input, index 1 must be int!")
words_dict={} #creating empty dictionary
text_file_path='D:\python codes\Word_Frequency_text.txt'
with open(text_file_path,'r') as file:
    # reading each line    
    for line in file:
        # reading each word        
        for word in line.split():
            # counting each word 
            # by creating key : value for every word in dictionary          
            if word in words_dict:
                words_dict[word]+=1
            else:
                words_dict[word]=1
#sorted list- most common words to least common words 
sorted_words_list=sorted(words_dict.items(), key=lambda item: item[1], reverse=True)
#Printing top N most common words
for i in range(N):
    print(str(i+1)+" - word: '"+str(sorted_words_list[i][0])+"' "+str(sorted_words_list[i][1])+" times")