import gensim.downloader as api
import numpy as np
import math

# 25, 50, 100 or 200. Số càng lớn thì càng chính xác, nhưng chạy càng lâu các bạn nhé
model = api.load("glove-twitter-200")
word = "beautiful"

print("6----------")
result = model.similarity("marriage", "happiness")
print(result)


#TODO: Các bạn thử viết 2 cách khác nhau để tính cosine similarity
# giữa 2 vector nhé. Kết quả giống với khi dùng model.similarity() là được
# 1 cách là dùng numpy, 1 cách là không dùng numpy nhé

world1="marriage"
world2="happiness"

#CACH 1: use Numpy
arr1=np.array(model[world1])
arr2=np.array(model[world2])
norm_arr1=np.linalg.norm(arr1)
norm_arr2=np.linalg.norm(arr2)
x=np.dot(arr1,arr2)/(norm_arr1*norm_arr2)
print("Cos cua goc hop boi 2 vector cua marriage va happiness khi tinh bang numpy: ", x)

#CACH 2: dung loop
def dot_product(a,b):
    dot=0
    for i, j in zip(a, b):
        dot+=i*j
    return dot
def norm_of_vector(vector):
    norm=0
    for i in vector:
        norm+=i*i
    return math.sqrt(norm)

def similarity_of_vector(vector1,vector2):
    return dot_product(vector1,vector2)/(norm_of_vector(vector1)*norm_of_vector(vector2))


y=similarity_of_vector(model[world1],model[world2])
print("Cos cua goc hop boi 2 vector cua marriage va happiness khi tinh bang loop: ", y)
