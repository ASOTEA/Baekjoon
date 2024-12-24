import sys

num = int(input())

a = list(map(int,sys.stdin.readline().split()))

a1 = sorted(a)

print(a1[0],a1[num -1])