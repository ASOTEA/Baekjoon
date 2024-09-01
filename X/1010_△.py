meno = {0: 1, 1: 1}

def factorial(n):
    if n in meno:
        return meno[n]
    if n > 1:
        temp = n*factorial(n-1)
        meno[n] = temp
        return temp    
    return 1

def f(N, M):
    c = factorial(M)//(factorial(M-N)*factorial(N))
    return c


T = int(input())


for i in range(T):
    N, M  = map(int, input().split())
    print(f(N, M))




## 나누기는 값을 넣어주고
### 굳이 힘들게 재귀로 함수를 안만들어도 된다.

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    bridge = factorial(m) // (factorial(n) * factorial(m - n))
    print(bridge)