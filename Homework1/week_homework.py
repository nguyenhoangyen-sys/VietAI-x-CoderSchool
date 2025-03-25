import re
from collections import deque

# Ex1: Write a program to count positive and negative numbers in a list
data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]

def CountNum(x):
    a=0
    b=0
    for i in x:
        if i > 0:
            a+=1
        else:
            b+=1
    return a, b

a, b = CountNum(data1)
print ("Ex1: there are " + str(a) + " positive number and " + str(b) + " negative numbers ")

# Ex2: Given a list, extract all elements whose frequency is greater than k.
data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3

def Extract(x,k):
    res = []
    for i in x:
        fre=x.count(i)
        if fre > k and i not in res:
            res.append(i)

    return res

list=Extract(data2,3)
print ("Ex2: the list of elements whose frequency is greater than k=3 " + str(list))

# Ex3: find the strongest neighbour. Given an array of N positive integers.
# The task is to find the maximum for every adjacent pair in the array.
data3 = [4, 5, 6, 7, 3, 9, 11, 2, 10]

def Strongest(x):
    res = []
    for i in range((len(x)-1)):
        if x[i] >= x[i+1]:
            res.append(x[i])
        else:
            res.append(x[i+1])

    return res
c=Strongest(data3)
print ("Ex3: the list of elements whose frequency is greater than k=3 " + str(c))

# Ex4: print all Possible Combinations from the three Digits
data4 = [1, 2, 3]

def Combinations(data, path =[]):
    if len(data) == len(path):
        print(path)
        return
    for i in data:
        if i not in path:
            Combinations(data, path + [i])

print("Ex4:")
d = Combinations(data4, path=[])

# Ex5: Given two matrices (2 nested lists), the task is to write a Python program
# to add elements to each row from initial matrix.
# For example: Input : test_list1 = [[4, 3, 5,], [1, 2, 3], [3, 7, 4]], test_list2 = [[1], [9], [8]]
# Output : [[4, 3, 5, 1], [1, 2, 3, 9], [3, 7, 4, 8]]
data5_list1 = [[4, 3, 5, ], [1, 2, 3], [3, 7, 4]]
data5_list2 = [[1, 3], [9, 3, 5, 7], [8]]

def add_element(list1, list2):
    for i in range((len(list1))):
        list1[i]+=list2[i]
    return list1
e=add_element(data5_list1,data5_list2)
print("Ex5: " + str(e))


# Ex6:  Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
arr=[]
for i in range(2000,3200):
    arr+=[i]

def divisible_by_7(arr):
    list = []
    for i in arr:
        if i % 7 ==0 and i % 5 !=0:
            list.append(i)
    return list
f = divisible_by_7(arr)
print("EX6: " + str(f))


# Ex7: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.




def even_digit_num():
    value = []
    for i in range(1000, 3000):
        s=str(i)
        if int(s[0])%2==0 and int(s[1])%2==0 and int(s[2])%2==0 and int(s[3])%2==0:
            value.append(str(i))

    return value
g = even_digit_num()
print("Ex7: "+",".join(g))


# Ex8: Let user type 2 words in English as input. Print out the output
# which is the shortest chain according to the following rules:
# - Each word in the chain has at least 3 letters
# - The 2 input words from user will be used as the first and the last words of the chain
# - 2 last letters of 1 word will be the same as 2 first letters of the next word in the chain
# - All the words are from the file wordsEn.txt
# - If there are multiple shortest chains, return any of them is sufficient

print("Ex8_part1: Type 2 words in English as input and Print out the output: "+"Hello World")




def wordLadder(start, target, arr):
    # set to keep track of unvisited words
    #st = set(arr)

    # store the current chain length
    res = 0
    #m = len(start)

    # queue to store words to visit
    words = deque()
    words.append(start)
    words_chain= []
    words_chain.append(start)

    while words:
        res += 1
        length = len(words)
        #print("so phan tu cua deque luc nay:",words)

        # iterate through all words at same level
        for _ in range(length):
            word = words.popleft()
            #print(word)

            # For
            for j in arr:

                if len(j)>=3 and word[-2:] == j[:2]:
                    arr.remove(j)
                    words.append(j)
                    words_chain.append(j)
                    #print("so phan tu cua deque luc nay:", words)
                    if j == target:
                        res+=1
                        words_chain_reverse = words_chain[::-1]
                        #print("words_chain: ", words_chain)
                        #print("words_chain_reverse: ",words_chain_reverse)
                        result=[words_chain_reverse[0]]
                        i = 0
                        while i < len(words_chain_reverse)-1:
                            for g in range(i+1, len(words_chain_reverse)):
                                if words_chain_reverse[i][:2]== words_chain_reverse[g][-2:]:
                                    #print("Lan lap nay i= ",i,"va g= ",g)
                                    result.append(words_chain_reverse[g])
                                    #print(result)
                                    i = g
                                    break

                                else:
                                    continue


                        result=result[::-1]
                        #print("We are at the end of while loop!!!!!")
                        return res,result


                else:
                    continue
    #print("world_chain:",words_chain)

    return 0


if __name__ == "__main__":
    arr = ["encroach", "enlarge", "envelope", "chutzpa", "chair", "parse", "papa", "pepper", "paper", "patrick", "poon", "plee", "same", "poie", "plie", "poin", "plea"]
    start = "pen"
    target = "paper"

    file_path = r"C:\Users\Lenovo\Desktop\VietAI-x-CoderSchool\Week1\wordsEn.txt"
    with open(file_path, 'r') as file:
        file_content = ''
        line = file.readline()

        while line:
            file_content += line
            line = file.readline()


    def remove_punctuation(text):
        text_lower_case = text.lower()
        return re.sub(r"[^\w\s'-]", '', text_lower_case)

    def create_arr(text):
        cleaned_text = remove_punctuation(text)
        tokens = re.split(r"[\s.,!]", cleaned_text)
        tokens = [token for token in tokens if token]  # Remove empty strings
        return tokens


    #cleaned_text=remove_punctuation(file_content)
    arr = create_arr(file_content)
    print(wordLadder(start, target, arr))