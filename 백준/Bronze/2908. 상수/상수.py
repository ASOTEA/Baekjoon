a ,b = input().split()
a1= []
b1 = []
for i in range(len(a)):
    a1.append(a[i])
for j in range(len(b)):
    b1.append(b[j])
a1.reverse()
b1.reverse()

a1 = ''.join(a1)
b1 = ''.join(b1)


if a1> b1:
    print(a1)
else:
    print(b1)
