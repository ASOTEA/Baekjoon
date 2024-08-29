meno = {1:1, 2:2, 3:3}

n = int(input())

def f(n):
    if n in meno:
        return meno[n]
    temp = (f(n-1)+ f(n-2))%10007
    meno[n] = temp
    return temp

print(f(n))


