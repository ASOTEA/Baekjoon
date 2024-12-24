import sys

n = int(sys.stdin.readline())

arr= []

for i in range(n):
    arr.append(int(sys.stdin.readline()))

set_arr = sorted(arr)

for i in set_arr:
    print(i)