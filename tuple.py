#NOT MUTABLE

tup = (1, 3, 32, 65, 11, 6, 25, 1)
# print(type(tup), tup)
# print(len(tup))
# print(tup[2],tup[5], tup[-3])
#
# print(tup)
# print(tup[5])
# print(tup[:5])
# print(tup[:-5]) #NegativeIndexing
# print(tup[5:])
# print(tup[2:6]) #RangeIndex
# print(tup[1:7:2])  #JumpIndex
#
# if 32 in tup:
#     print("Present")
#
# tup1 = tup[2:6]
# print(tup, tup1)
# print(tup.index(6))    #index method
# print(tup.count(5))    #count method
#
# l = (100, 250, 6, 25)
# k = l + tup          #tup concatenating
# print(k)


#Methods on tuple
# t = list(tup)           #convert tuple into list
# t.append(5)        #appending the converted tuple-list
# print(t)
# t.pop(8)        #remove item
# print(t)
# t[2] = 30      #change item
# print(t)
# tup = tuple(t)      #converting list into tuple
# print(t)
tup1 = (5, 25, 62, 26, 10, 100)
tupple = tup + tup1

# print(tupple)
# res = tupple.count(1)       #count the number accordance
# res = tupple.index(1)       #indexing the number accordance
# res = tupple.index(1, 3, 9)     #indexing the number accordance in range
res = len(tupple)
print(res)