a = []
i = 0
while i <9:
    num = int(input())
    a.append(num)
    i  = i + 1
a1 = sorted(a)

print(a1[8])
b= a.index(a1[8])
print(b+1)
