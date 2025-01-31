def mygen():

    for i in range (50):
        # i = i + 1
        yield i
    # l = 1
    # while l <= n:
    #     yield l
    #     l = l + 1

# gen = mygen()
# # print(list(gen))
# print(gen)

#for j in gen:
    # print(j)

for j in mygen():
    print(j)