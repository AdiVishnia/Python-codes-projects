import sys

try:
    N=int(sys.argv[1]) #input N from user by using sys.argv
except:
    print("Invalid input, index 1 must be int!")
words_dict={} #creating empty dictionary
# opening the text file
with open('text.txt','r') as file:
    # reading each line    
    for line in file:
        # reading each word        
        for word in line.split():
            # counting each word 
            # by creating key : value for every word in dictionary          
            if word in words_dict:
                words_dict[word]+=1
            else:
                words_dict[word]=0
#sorted list- most common words to least common words 
sorted_words_list=list(sorted(words_dict.items(), key=lambda item: item[1], reverse=True))
#Printing top N most common words
for i in range(N):
    print(str(i+1)+" - word: '"+str(sorted_words_list[i][0])+"' "+str(sorted_words_list[i][1])+" times")