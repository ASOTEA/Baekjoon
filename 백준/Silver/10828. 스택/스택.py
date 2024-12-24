import sys



# N = int(input())
N = int(sys.stdin.readline()) 

d = []
for _ in range(N):
    # a = input().split()
    a = sys.stdin.readline().split()
    if a[0] == 'push':
        d.append(int(a[1]))

    
    if a[0] == 'top':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
    
    if a[0] == 'pop':
        if len(d) ==0:
            print(-1)
        else:
            print(d.pop())
    
    if a[0] == 'size':
        print(len(d))

    if a[0] == 'empty':
        if len(d) ==0:
            print(1)
        else:
            print(0)