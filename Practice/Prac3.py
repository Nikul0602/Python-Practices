## CREATING A KBC USING LIST AND DICTIONARY

q = [
    ["In Which country diwali is celebrated?", "Bharat", "Australia", "US", "Pakistan", None, 0],
    ["What is the famous sweet of Surat District of Gujarat?", "Gulab Jamun", "Ras Gulla", "Ghaari", "Mohanthaal", None,
     3],
    ["What is the most ancient thing in india?", "Hadappa", "Kailash Parvat", "Gold", "Silver", None, 2]]

amt = [5000,
       10000,
       15000]

winning = 0

for i in range(0, len(q)):
    qs = q[i]
    print(f"Question for Rs. {amt[i]}.", q[i])
    print(f"a. {qs[1]},   b. {qs[2]} ")
    print(f"c. {qs[3]},   d. {qs[4]} ")
    ua = int(input("Provide a answer (1-4): "))

    if ua == qs[-1]:
        winning += amt[i]
        print(f"Congrats!, You won ₹ {winning}")

    else:
        print("Sorry! Wrong answer")
        print(f"Your total Winning is ₹ {winning}")
        break

print("You're total Winning amount is: ", "₹", winning)


