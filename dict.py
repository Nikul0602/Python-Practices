# This is a converted Python file
## DICTIONARY BASICS

# names = {"fname" : "Nikul", "lname" : "Prajapati"}
#
# print(names["fname"],names["lname"])

# reg = {
#     1 : "Nikul",
#     2 : "Jay",
#     3 : "Pritesh",
# }

# print(reg.keys())
# print(reg['name'])            #generate error if key is not exist
# print(reg.get('name'))        #gives None if key is not exist

# for key in reg.keys():
#     print(reg[key])
# for key in reg.keys():
#     print(f"The value corresponding to the key {key} is {reg[key]}")

# print(reg.items())
#
# for key, value in reg.items():
#     print(f"The value corresponding to the key {key} is {value}")


## DICTIONARY METHODS
m = {
    "Nikul" : 79,
    "Jay" : 80,
    "Pritesh" : 89
}

m1 = {
    "Bhargav" : 72,
    "Aniket" : 76,
    "Krunal" : 77
}

print(m)
# print(m1)
# m.update(m1)
# m1.clear()
# m.pop("Jay")          #remove the specific key:value from the dictionary
# m.popitem()           #removes the last key:value from the dictionary
# del m                 #delete entire dictionary
# del m["Jay"]            #remove the specific key:value from the dictionary
print(m)
# End of converted file