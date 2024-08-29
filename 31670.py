import sys
sys.setrecursionlimit(10**6)

meno = {1:0}
n = int(input())
R = list(map(int, input().split(' ')))


if n >= 2:
    meno[2]=  min(R[0], R[1])
if n >= 3:
    meno[3]= min(R[0]+R[2], R[1])


def d(n):
    global R
    if n in meno:
        return meno[n]

    temp = min(d(n-1)+R[n-1], d(n-2)+R[n-2])
    meno[n] = temp
    return temp

print(d(n))
