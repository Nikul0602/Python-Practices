# num = int(input("Enter number of rows:"))
# boolean = int(input("enter t/f\n"))
# b = bool(boolean)
# if b == 1:
#     for i in range(num):  # i=0
#         for j in range(i + 1):  # j=0 (4)
#             print("*", end="")
#         print("")
# else:
#     for i in range(num):  # 0,1,2,3 i=0
#         for j in range(num-i):  # j=3,
#             print("*", end="")
#         print()
#

#diamond
# a = int(input("enter number: "))
# for i in range(a):
#     for j in range(a - i):
#         print(end = "  ")
#     for j in range(1, i * 2):
#         print("*", end = " ")
#     print()
# for i in range(a, 0, -1):
#     for j in range(a - i):
#         print(end = "  ")
#     for j in range(1, i * 2):
#         print("*", end = " ")
#     print()

# for i in range(a, 0, -1):
#     print("* " * i)


#pyramid
a = 0
b = 1
n = int(input("Enter range for series: "))

for i in range(n):
    print(a, end = " ")
    sum = a + b
    a = b
    b = sum

print("             ")

