num = input()

k = 0
if len(num)==1:
    a1 = 0
    a2 = int(num[0])
    while True:
        b1 = a1+ a2
        if b1>=10:
            b1 = b1%10
        a1 = a2
        a2 = b1
        k = k+1
        if a1 == 0 and a2 == int(num[0]):
            print(k)
            break
        else:
            continue

else:
    a1 = int(num[0])
    a2 = int(num[1])
    while True:
        b1 = a1 + a2

        if b1>=10:
            b1 = b1%10
        a1 = a2
        a2 = b1
        k= k+1
        if a1 == int(num[0]) and a2 == int(num[1]):
            print(k)
            break
        else:
            continue
