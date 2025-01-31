
# a = open(filename: 'file.txt', mode of file: 'r')
# mode of file :
# 'a' = for append the text
# 'r' = to open file in read only mode
# 'w' = to open file in write mode
# a = open('file.txt', 'r')
#
# b = a.read()
# print(b)
# a.close()

##  FUNCTIONS FOR FILE HANDLING

#READ FILE LINE BY LINE
# a = open('file.txt', 'r')
# i = 0
# while True:
#     i = i + 1
#     line = a.readline()
#     if not line:
#         break
#     r1 = line.split(",")[0]
#     print(f"Roll no. {i} is {r1}")


#WRITE INTO FILE LINE BY LINE
# a = open('file.txt', 'a')
# lines = ['\nAniket,\n', 'Krunal,\n', 'Bhargav\n']
# a.writelines(lines)
# a.close()

#SEEK AND TELL FUNCTIONS
# with open('file.txt', 'r') as a:
#     print(type(a))
#     a.seek(6) ## will start read file after 6 characters
#
#
#     print(a.tell())  ## will tell on which position of character we are on right now.
#     data = a.read(4) ## will read first 4 characters after seek()
#     print(data)
#

## TRUNCATE FUNCTION
with open('file1.txt', 'w') as b:
    b.write('Hello! Nikul')
    b.truncate(12)  ## will ensure how many character should be get printed in file

with open('file1.txt', 'r') as b:
    print(b.read())