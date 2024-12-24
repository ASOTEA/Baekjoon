import sys

k = int(sys.stdin.readline())
j=[]
e= []

for i in range(k):
    a,b= sys.stdin.readline().split()
    a =int(a)
    b= int(b)
    j.append(a)
    e.append(b)

for i in range(k):
    print(j[i]+e[i])
    
