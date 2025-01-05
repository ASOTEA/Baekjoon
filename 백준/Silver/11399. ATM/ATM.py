import sys
input = sys.stdin.readline


N = int(input())

lst = list(map(int, input().split()))
lst.sort()
result_lst = []


for i in range(len(lst)):
    if i == 0:
        result_lst.append(lst[0])
    else:
        result_lst.append(result_lst[i-1] + lst[i])
    # print(result_lst)

print(sum(result_lst))