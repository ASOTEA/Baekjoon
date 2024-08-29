
n = int(input())

meno = {0:0, 1:1}
def f(n):
    if n in meno:
        return meno[n]
    else:
        temp = f(n-1) + f(n-2)
        meno[n] = temp
        return temp
    
print(f(n))