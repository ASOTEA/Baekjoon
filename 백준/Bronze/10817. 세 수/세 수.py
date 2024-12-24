a, b, c= input().split()

a= int(a)
b = int(b)
c = int(c)

if a < b:
    if b < c:
        print(b)
    else:
        if a < c:
            print(c)
        else:
            print(a)
else:
    if c < b:
        print(b)
    else:
        if a< c:
            print(a)
        else:
            print(c)
