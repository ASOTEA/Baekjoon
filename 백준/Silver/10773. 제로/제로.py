N = int(input())
lst = []

for i in range(N):
    add = int(input())
    if add == 0:
        lst.pop()
    else:
        lst.append(add)

print(sum(lst))