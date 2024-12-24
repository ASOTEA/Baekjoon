N  = input()

num = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for j in num:
    for i in range(len(N)):
        if j== N[i]:
            print(i,end="")
            break
    if j in N :
        print('',end=' ')
    else:
        print(-1, end= ' ')
