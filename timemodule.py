import time
#
def usingwhile():
    i = 0
    while i < 5000:
        i = i + 1
        print(i)

def usingfor():
    for i in range(5000):
        print(i)

init = time.time()
usingwhile()
t1 = time.time() - init
usingfor()
t2 = time.time() - init

print(t1)
print(t2)

# print(5)
# time.sleep(3)
# print(f"This is Printed after 3 seconds")

# t = time.localtime()
# formatted_item = time.strftime("%Y-%m-%d  %H:%M:%S", t)
# print(formatted_item)