# # Try to open and read the content of the renamed file
# with open('requirements.txt', 'r', encoding='utf-8', errors='ignore') as f:
#     content = f.read()
#
#
# cleaned = ''.join(content.split())
#
# print(cleaned)
#
# with open('requirements_cleaned.txt', 'w', encoding='utf-8', errors='ignore') as file:
#     file.write(cleaned)
#
# print("Done")

# n = int(input("Enter Number : "))
# def fib(n):
#     r, a, b = [], 0, 1
#     while a < n:
#         r.append(a)
#         a, b = b, a+b
#     # print(r)
#     return r

# f = fib(n)
# print(f)


# a, b = 0, 1
# print([a := b if (a := a) or False else a for _ in range(10)])


a = [1,2,5,4,6,7,8,9,10]

longest = []
current = [a[0]]

for i in range(1, len(a)):
    if a[i] == a[i-1]+1:
        current.append(a[i])
    elif len(current) > len(longest):
        longest = current
    else:
        current = [a[i]]

if len(current) > len(longest):
    longest = current

print(longest)