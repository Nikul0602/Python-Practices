a = 5
print(a)

def hi():
    b = 6
    global a  # To change value of global variable define outside of function.
    a = "n"      f'''\n{{a = "n"}}This will change the value of a 5 to "n"'''
    print(f"this is local var {b}")
    print("Hiiiiii")

print(f"this is global var {a}")
hi()
print(f"this is global var {a}")
# print(f"this is local var {b}")