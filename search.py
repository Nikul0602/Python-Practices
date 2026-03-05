# def binary_search(a, key):
#     low = 0
#     high = len(a) - 1
#
#     while low <= high:
#         mid = (low + high)//2
#
#         if a[mid] == key:
#             return mid
#         elif a[mid] < key:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1


# def linear_search(arr,key):
#
#     for i in range(len(arr)):
#         if arr[i] == key:
#             return i
#
#     return -1
#
# a = [1,2,3,4,5,6,7,8,9]
# # print(binary_search(a, 6))
# print(linear_search(a, 0))



# token generation
# import secrets
# import string
#
# CHARSET = string.digits + string.ascii_letters + "@#$%*"
#
# def generate_token(length=9):
#     return ''.join(secrets.choice(CHARSET) for _ in range(length))
#
# token = generate_token()
# print(token)


a = [1,2,3]
b = [4,5,3]

for i in range(len(b)):
    if b[i] in a:
        continue
    else:
        a.append(b[i])

print(a)