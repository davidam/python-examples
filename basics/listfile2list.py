from ast import literal_eval
with open('list.txt') as f:
    mainlist = [list(literal_eval(line)) for line in f]

l = mainlist[0]

print(l)

# ll = []
# for i in l:
#     ll.append(i.split())

#print(ll)    

# x = 0
# y = 0
# for j in ll:
#     if (len(j[0]) == 1):
#         x = x + 1
#     else:
#         y = y + 1
# print(y)
# print(x)
# for i in l:
#     print(i)
