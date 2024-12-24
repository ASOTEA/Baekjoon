def even(k):
    if len(k) % 2 > 0:
        return 'NO'
    return divide(lst)

def divide(lst):
    if lst.count('(') != len(lst)//2:
        return 'NO'
    return func(lst)

def func(lst):
    cnt = 0

    for i in lst:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1

        if cnt < 0:
            return 'NO'
            break
    
    if cnt == 0:
        return 'YES'
    else:
        return 'NO'


arr = []


n = int(input())

for i in range(n):
    lst = list(map(str, input()))

    arr.append(even(lst))


for i in arr:
    print(i)

