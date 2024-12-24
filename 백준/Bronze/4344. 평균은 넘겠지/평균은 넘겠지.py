def num ():
    a= list(map(int,input().split()))
    k= -a[0]

    for i in range(len(a)):
        k = k +a[i]
    k = k/a[0]
    e = 0
    for j in range(1,len(a)):
        if k < a[j]:
            e = e+1
    total =(e/a[0]*100)
    return total


agr = []

x = int(input())
for i in range(x):
    agr.append(num())

for j in range(x):
    print("%.3f%%"%agr[j])
