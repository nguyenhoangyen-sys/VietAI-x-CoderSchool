
import numpy as np
import re

# Ex1: Write a NumPy program to reverse an array (first element becomes last).
# Input: [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]


# Creating an array 'x' using arange() function with values from 12 to 37 (inclusive)
x = np.arange(12, 38)

# Printing the original array 'x' containing values from 12 to 37
print("Ex1:")
print("Original array:")
print(x)

# Reversing the elements in the array 'x' and printing the reversed array
print("Reverse array:")
x = x[::-1]
print(x)

# Ex2: Write a NumPy program to test whether each element of a 1-D array is also present in a second array
# Input Array1: [ 0 10 20 40 60]
#       Array2: [10, 30, 40]
print("Ex2:")
arr1=np.array([0,10,20,40,60])
print("array 1:"+ str(arr1))
arr2=np.array([10,30,40])
print("array 2:"+ str(arr2))

x=np.in1d(arr1,arr2)
print("Test whether each element in array 1 exists in array 2: \n "+str(x))

# Ex3: Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array
# Input Array [1,6,4,8,9,-4,-2,11]

array=np.array([1,6,4,8,9,-4,-2,11])

print("Ex3: my array:"+ str(array))

print("Max of my array:",array[np.argmax(array)])

print("Min of my array:",array[np.argmin(array)])

# Ex4: Read the entire file story.txt and write a program to print out top 100 words occur most
# frequently and their corresponding appearance. You could ignore all
# punction characters such as comma, dot, semicolon, ...
# Sample output:
# house: 453
# dog: 440
# people: 312
# ...


file_path=r"C:\Users\Lenovo\Desktop\VietAI-x-CoderSchool\Week2\story.txt"
#with open(file_path, 'r') as file:
    #file_content = file.read()

with open(file_path, 'r') as file:
    file_content = ''
    line = file.readline()

    while line:
        file_content += line
        line = file.readline()


def remove_punctuation(text):
    text_lower_case = text.lower()
    return re.sub(r"[^\w\s'-]", '', text_lower_case)



#print(cleaned_text)

#new_list = []
#for word in cleaned_text.split(" "):
    #new_list.append(word)
#print(new_list)
def split_words(text):
    cleaned_text = remove_punctuation(text)
    tokens = re.split(r"[\s.,!]", cleaned_text)
    tokens = [token for token in tokens if token]  # Remove empty strings
    return tokens

#cleaned_text=remove_punctuation(file_content)
tokens=split_words(file_content)
print(len(tokens))
#print(tokens)



def frequency_of_word(arr, n):
    # freq to store the freq of the most occurring variable
    #freq = 0

    # res to store the most occurring string in the array of strings
    my_dict = dict()

    # running nested for loops to find the most occurring
    # word in the array of strings
    for i in range(0, n, 1):
        count = 1
        for j in range(i + 1, n, 1):
            if arr[j] == arr[i]:
                count += 1


        # updating our max freq of occurred string in the
        # array of strings

        #print("my"+ str(i)+ " interation: ",arr[i],count)
        if arr[i] not in my_dict:
            my_dict[arr[i]] = count
        #count = 1


    #print("the words that occur : " + str(my_dict))
    result={k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1], reverse=True)}
    #print(result)

    print("Ex4: top 100 words occur most frequently and their corresponding appearance")
    num=0
    for x, y in result.items():
        print(x,": ",y)
        num += 1
        if num == 100:
            break
    return 0




# Driver code

# given set of keys
#arr = ["geeks", "for", "geeks", "a", "portal", "to", "learn", "can", "be", "computer", "science", "zoom", "yup", "fire",
       #"in", "be", "data", "geeks", ]
#n = len(arr2)

#arr2=['file', 'was', 'produced', 'from', 'images', 'generously', 'made', 'available', 'by', 'the', 'university', 'of', 'florida', 'digital', 'collections', "alice's", 'adventures', 'in', 'wonderland', 'illustration', 'alice', 'illustration', "alice'sâadventures", 'inâwonderland', 'byâlewisâcarroll', 'illustratedâby', 'arthurârackham', 'with', 'a', 'proem', 'by', 'austin', 'dobson', 'londonâwilliamâheinemann', 'newâyorkâdoubledayâpageââco', 'printed', 'in', 'england', "'tis", 'two', 'score', 'years', 'since', "carroll's", 'art', 'with', 'topsyturvy', 'magic', 'sent', 'alice', 'wondering', 'through', 'a', 'part', 'halfcomic', 'and', 'halftragic', 'enchanting', 'alice', 'blackandwhite', 'has', 'made', 'your', 'deeds', 'perennial', 'and', 'naught', 'save', 'chaos', 'and']
#arr1= ['ï»¿Project', "Gutenberg's", "Alice's", 'Adventures', 'in', 'Wonderland', 'by', 'Lewis', 'Carroll', 'This', 'eBook', 'is', 'for', 'the', 'use', 'of', 'anyone', 'anywhere', 'at', 'no', 'cost', 'and', 'with', 'almost', 'no', 'restrictions', 'whatsoever', 'You', 'may', 'copy', 'it', 'give', 'it', 'away', 'or', 'reuse', 'it', 'under', 'the', 'terms', 'of', 'the', 'Project', 'Gutenberg', 'License', 'included', 'with', 'this', 'eBook', 'or', 'online', 'at', 'www', 'gutenberg', 'net', 'Title:', "Alice's", 'Adventures', 'in', 'Wonderland', 'Illustrated', 'by', 'Arthur', 'Rackham', 'With', 'a', 'Proem', 'by', 'Austin', 'Dobson', 'Author:', 'Lewis', 'Carroll', 'Illustrator:', 'Arthur', 'Rackham', 'Release', 'Date:', 'May', '19', '2009', '[EBook', '#28885]', 'Language:', 'English', '***', 'START', 'OF', 'THIS', 'PROJECT', 'GUTENBERG', 'EBOOK', "ALICE'S", 'ADVENTURES', 'IN', 'WONDERLAND', '***', 'Produced', 'by', 'Jana', 'Srna', 'Emmy', 'and', 'the', 'Online', 'Distributed', 'Proofreading', 'Team', 'at', 'http://www', 'pgdp', 'net', '(This', 'file', 'was', 'produced', 'from', 'images', 'generously', 'made', 'available', 'by', 'the', 'University', 'of', 'Florida', ]
# function call
frequency_of_word(tokens,len(tokens))


