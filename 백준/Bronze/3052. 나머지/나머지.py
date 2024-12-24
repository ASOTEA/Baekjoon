num = []
x = 0
y = []
for i in range(10):
    a = int(input())
    num.append(a)

for j in range(10):
    x=num[j]%42
    y.append(x)
    y.sort()
ten= 10

for e in range(9):
    if y[e] == y[e+1]:
        ten = ten -1
print(ten)