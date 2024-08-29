meno = {41:0, 42:0, 1:1, 2:1}


def f(n):
    if n in meno:
        return meno[n]
    else:
        meno[42]+=1
        temp = f(n-1) + f(n-2)
        meno[n] = temp
        return temp

n = int(input())
print(f(n),meno[42])