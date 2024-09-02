

def f(x):
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            return False
    return True

N, M = map(int, input().split())

for i in range(N, M+1):
    if i ==1:
        continue
    if f(i):
        print(i)