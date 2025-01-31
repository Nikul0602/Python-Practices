## Normal function

# def square(a):
#     return a*a
#
# print(square(9))


## LAMBDA FUNCTION
# def num(f, val):
#     return 5 + f(val)
#
# square = lambda a: a*a
# Add = lambda a = 5, b = 6: a + b
#
# print(square(6))
# print(Add(9, -3))
# print(num(square, 15 ))
# print(num(lambda a = 5, b = 6: a + b, 15 ))

## MAP, FILTER AND REDUCE FUNCTIONS

## MAP

# def cube(a):
#     return a * a * a
#
# print(cube(4))

l = [2, 5, 6, 8, 3, 1]
# normal method
# l1 = []
#
# for item in l:
#     l1.append(cube(item))
# same method with map() function
# l1 = list(map(cube, l))
# l2 = tuple(map(lambda a: a * a * a, l))
# l3 = set(map(cube, l))
# print(l1)
# print(l2)
# print(l3)


## FILTER

# def filter_func(a):
#     return a > 4
# l1 = list(filter(lambda a: a > 4, l))
# l2 = tuple(filter(filter_func, l))
# l3 = set(filter(filter_func, l))
# print(l1)
# print(l1)
# print(l2)
# print(l3)

## REDUCE
from functools import reduce


num = [1, 2, 5, 6, 8, 8]
#Explaination of how reduce works:
# num = [(1+2)=3, 5,6,8,8]
# num = [(3+5)=8,6,8,8]
# num = [(8+6)=14, 8,8]
# num = [(14+8)=22,8]
# num = [(22+8) = 30]
# num = "final output" 30

def mysum(x, y):
    return x + y

sum = reduce(mysum, num)
sum1 = reduce(lambda a, b: a+b, num)

print(sum)
print(sum1)