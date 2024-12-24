
N = int(input())

lst = [i for i in range(1, N+1)]

value = []


for i in range(len(lst)):
    if len(lst) == 0:
        break
    value.append(lst.pop(0))
    if len(lst) == 0:
        break
    lst.append(lst.pop(0))


for i in value:
    print(i , end = ' ')