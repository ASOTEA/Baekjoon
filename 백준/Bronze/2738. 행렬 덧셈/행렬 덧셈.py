n, m = map(int, input().split())
arr = []
for i in range(n):
    lst = list(map(int, input().split()))
    arr.append(lst)

for i in range(n):
    lst_2 = list(map(int, input().split()))
    arr[i] = [str(x+y) for x, y in zip(arr[i], lst_2)]

for i in arr:
    print(' '.join(i))
