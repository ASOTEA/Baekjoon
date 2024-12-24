num = int(input())

a = [] 
for i in range(num):
    H, W, N = map(int, input().split())
    
    floor = N%H
    num = N//H +1

    if N%H == 0:
        floor = H
        num = N//H
    a.append(floor*100 + num)

for _ in a:
    print(_)