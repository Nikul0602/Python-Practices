# # # Try to open and read the content of the renamed file
# # with open('requirements.txt', 'r', encoding='utf-8', errors='ignore') as f:
# #     content = f.read()
# #
# #
# # cleaned = ''.join(content.split())
# #
# # print(cleaned)
# #
# # with open('requirements_cleaned.txt', 'w', encoding='utf-8', errors='ignore') as file:
# #     file.write(cleaned)
# #
# # print("Done")

# # n = int(input("Enter Number : "))
# # def fib(n):
# #     r, a, b = [], 0, 1
# #     while a < n:
# #         r.append(a)
# #         a, b = b, a+b
# #     # print(r)
# #     return r

# # f = fib(n)
# # print(f)


# # a, b = 0, 1
# # print([a := b if (a := a) or False else a for _ in range(10)])


# a = [1,2,5,4,6,7,8,9,10]

# longest = []
# current = [a[0]]

# for i in range(1, len(a)):
#     if a[i] == a[i-1]+1:
#         current.append(a[i])
#     elif len(current) > len(longest):
#         longest = current
#     else:
#         current = [a[i]]

# if len(current) > len(longest):
#     longest = current

# print(longest)

# import copy

# a = [[1,2],[3,4]]

# b = copy.copy(a)       # shallow copy
# c = copy.deepcopy(a)   # deep copy

# b[0][0] = 99
# c[1][1] = 88

# print("a:", a)
# print("b:", b)
# print("c:", c)

# s = "AI engineer interview"
# print(" ".join(s.split()[::-1]))

# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)

# print(fib(20))

from functools import lru_cache

# @lru_cache(maxsize=128)
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)

# print(fib.cache_info())
# print(fib(40))
# print(fib.cache_info())
# print(fib(50))
# print(fib.cache_info())
# print(fib(40))
# fib.cache_clear()
# print(fib.cache_info())



# @lru_cache()
# def test(a):
#     return sum(a)

# test([1,2,3]) 

# import numpy as np
# from sklearn.metrics.pairwise import cosine_similarity

# # Example vectors (pretend they are embeddings)
# query = np.array([[0.9, 0.1, 0.3]])

# documents = np.array([
#     [0.8, 0.2, 0.3],   # doc1
#     [0.1, 0.9, 0.2],   # doc2
#     [0.85, 0.05, 0.25] # doc3
# ])

# similarities = cosine_similarity(query, documents)

# print(similarities)

from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

documents = [
    "How to become an AI engineer",
    "Best pizza recipe",
    "Machine learning career guide"
]

query = "How can I start a career in AI?"

# Convert text to embeddings
doc_embeddings = model.encode(documents)
query_embedding = model.encode(query)

# Calculate similarity
scores = util.cos_sim(query_embedding, doc_embeddings)

print(scores)