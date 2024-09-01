lst = []
for x, y in zip(*[iter(input().split())]*2):
    lst.append([x,y])

print(lst)




