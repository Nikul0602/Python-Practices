# FOR LOOP

# a = 0
#
# for i in range(1, 12, 6):
#     # a +=1
#     print(i)
#
# colors = ["Red", "Green", "Blue", "White", "Black"]
#
# for color in colors:
#     print(color)
#     for i in color:
#         print(i)


# WHILE LOOP

# while (a<=20):
#     a = int(input("enter number:"))
#     print(a)
#     if (a <= 20):
#         print("Please enter number which bigger than 20")


#BREAK AND CONTINUE STATEMENT

# for i in range(20):
#     if (i == 10):
#         break
#     print("5 x", i+1, "=", 5 * (i+1))


# for i in range(20):
#     if (i == 10):
#         continue
#     print("5 x", i+1, "=", 5 * (i+1))


#DO-WHILE EMULATION
a = int(input("enter positive number:"))
while True:
    print(a)
    a +=1
    if (a%100 != 0):
        print("Entered Number",a," is not devided by 100")
    else:
        print(a)
        print("entered Number",a," is devided by 100")
        break