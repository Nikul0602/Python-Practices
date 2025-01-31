a = int(input("Enter the value of a:"))

ln = a

match a:
    case 0:
        print(a," is Zero")

    case _ if a%2 == 0:
        print(a, " is even")

    case _:
        print(a, "is odd")

while ln % 2 == 0 and ln > 1:
    ln = ln // 2

print("The last remaining number was:", ln)