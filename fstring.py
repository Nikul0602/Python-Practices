# This is a converted Python file
while True:
    try:
        a = int(input("Enter number: "))
        print(f"Multiplication table of {a} is: ")
        if a <= 0:
            raise ValueError("You can't generate a Multiplication table for zero or Negative Value")

        elif a > 0:
            for i in range(1, 11):
                print(f"{int(a)} x {i} = {int(a) * i}")
            break
    except ValueError as e:
                print(e)


print(f"The Multipication Table for {a} is done.")

# End of converted file