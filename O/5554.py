lst = []

for _ in range(4):
    lst.append(int(input()))
x, y = divmod(sum(lst), 60)
print(x)
print(y)