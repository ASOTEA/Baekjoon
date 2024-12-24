N = int(input())


for i in range(N):
    a,b = input().split()
    a = int(a)
    for i in b:
        print(i*a,end='')
    print('')