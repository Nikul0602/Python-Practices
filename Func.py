#DEFINING FUNCTIONS
#
# def gmean(a, b):
#     mean = (a * b)/(a + b)
#     print(mean)
#
# def isgreater(a, b):
#     if a>b:
#         print("First number is greater")
#     elif a == b:
#         print("Both numbers are equal")
#     else:
#         print("Second number is greater")
#
# a = 24
# b = 24
# gmean(a, b)
# isgreater(a, b)
#
#
# c = 2.5
# d = 6.3
# gmean(c, d)
# isgreater(c, d)
#
# e = 9
# f = 6
# gmean(e, f)
# isgreater(e, f)


#FUNCTION ARGUMENTS

#default arguments
# def name(fname = "Nikul", lname = "Prajapati"):
#     print("Hello", fname, lname)
# name()

#keyword argument
# def average(a=6, b=4):
#     print("average of",a,"and",b," is:", (a+b)/2)
# average(b = 25, a = 35)

#required argument
# def average(a, b, c = 5):
#     print("average of",a,",",b,"and",c," is:", (a + b + c)/2)
# average(100, 25)

##Variable-length arguments
#arbitrary arguments
#
# def average(*numbers):
#     #print(type(numbers))
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print("Average of",numbers," is: ", sum/len(numbers))
#
# average(10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 5)

#Keyword arbitrary arguments
# def name(**name):
#     #print(type(name))
#     print("Hello,", name["fname"],name["mname"], name["lname"])
#
# name(mname = "Kumar", lname="Prajapati", fname="Nikul")


#RETURN STATEMENT
def average(*numbers):
    #print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    #return 6
    return sum/len(numbers)

a = average(10, 20, 30, 40)
print(a)