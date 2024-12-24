import sys

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))


meno = [0]
temp = 0

for i in lst:
    temp += i
    meno.append(temp) 


for _ in range(M):
    i , j = map(int, sys.stdin.readline().split())

    print(meno[j]- meno[i-1])
