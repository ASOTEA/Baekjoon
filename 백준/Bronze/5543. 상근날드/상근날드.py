a = int(input())            
b = int(input())
c = int(input())
d = int(input())           
e = int(input())

if a < b:
    if a < c:
        k = a
    else:
        k = c
else:
    if a<c:
        k =b
    else:
        if b<c:
            k = b
        else:
            k = c

if d < e:
    i = d
else:
    i = e
print(k+i-50)
