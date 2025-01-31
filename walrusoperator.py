#IT DEFINES WITH :=

# a = True
# print(a)
# print(a:=False)

## WALRUS OPERATOR IN WHILE LOOP

# number = [1,2,3,4,5,6,7]
#
# while n:= len(number) > 0:
#     print(number.pop())

# foods = list()
# while True:
#     food = input("Enter your Favorite Food Name: ")
#     if food == "quit":
#         break
#     foods.append(food)
#
# print(f"You have entered food names are: {foods}")

# foods = list()
# while (food := input("Enter your Favorite Food Name: ")) != "quit" :
#     foods.append(food)
#
# print(f"You have entered food names are: \n{foods}")

# numbers = [2, 8, 0, 1, 1, 9, 7, 7]
#
# description = {
#     "length": len(numbers),
#      "sum": sum(numbers),
#     "mean": sum(numbers) / len(numbers),
# }
#
# print(description)

# num = [2, 8, 0, 1, 1, 9, 7, 7]
#
# length = len(num)
# sum  = sum(num)
#
# desc = {
#     "length": length,
#      "sum": sum,
#     "mean": sum / length,
# }
#
# print(desc)


## Walrus operator
num = [2, 8, 0, 1, 1, 9, 7, 7]

desc = {
    "length": (length := len(num)),
     "sum": (sum  := sum(num)),
    "mean": sum / length,
}
print(desc['length'],desc['sum'],desc['mean'])