import time

# ts = input(time.strftime('%H:%M:%S'))
h = int(time.strftime('%H'))
# h = int(input("Enter Hour: "))
print(h)
#
# ts = time.strftime('%M')
# print(ts)
#
# ts = time.strftime('%S')
# print(ts)

if (h>00 and h<12):
    print("Morning")
elif (h>12 and h<18):
    print("Afternoon")
else:
    print("Good Night")

# name = input('Enter your name: ')
# recenttime = time.strftime('%H:%M:%S')
# Recenttime = int(time.strftime('%H'))
# c= name.capitalize()
# if(4<=Recenttime<12):
#     print('GOOD MORNING',c,'its',recenttime)
# elif(12>=Recenttime<17):
#     print('GOOD EVENING',c,'its',recenttime)
# else:
#     print('GOOD NIGHT',c,'its',recenttime)