## Calculating factorial

# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(3) = 3*2*1
# factorial(2) = 2*1
# factorial(1) = 1
# factorial(0) = 1


# factorial(n) = n * factorial(n - 1)


# def factorial(n):
#     if (n==0 or n == 1):
#         return 1
#     else:
#         return n * factorial(n - 1)


# n = int(input("Enter number for factorial: "))

# print(factorial(n))
# print(factorial(4))
# print(factorial(5))


## Calculating Fibonacci series

def Fibonacci(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return (Fibonacci(n - 1) + Fibonacci(n - 2))


n = int(input("Enter number for series: "))

if (n <= 0):
    print("Enter positive number")

# print(Fibonacci(n))
else:
    # sum = 0
    for i in range(n):
        # a = Fibonacci(i)
        print(Fibonacci(i), end=" ")
        # sum += a
    print("\nsum is:", sum)

