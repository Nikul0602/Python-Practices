# from PIL.ImagePalette import negative

# a = int(input("Enter number:"))

# print("Entered age is:", a)
#
# if(a>18):
#     print("Congrats!, You can drive a car.")
# elif(a==18):
#     print("You're eligible to drive a car, But be careful you're still young.")
# else:
#     print("Sorry, you cannot drive a car as you're not 18 years old.")

## nested if statement

# for i in range (a):
#     if a<0:
#         print("Negative")
#     elif a==0:
#         print ("Zero")
#     else:
#         print("Positive")


# if a<0:
#
#     print("Negative")
# elif a>0:
#     if a <= 10:
#         print('''Positive and''',"In Range of 1-10")
#     elif 10 < a <= 20:
#         print('''Positive and''',"In Range of 11-20")
#     else:
#         print('''Positive and''',"Greater than 20.")
# else:
#     print("Zero")


## SHORT HAND IF-ELSE STATEMENT
a = 250
b =25

print(f"the bigger number is a {a}") if a > b else print(f"a = {a} and b = {b} are equal") if a == b else print(f"The smaller number is b {b}")

# import os
#
# os.remove("shortifelse.py")

# import os
# #
# if os.path.exists("hi.ipynb"):
#     os.remove("hi.ipynb")
# else:
#     print("path does not exist")