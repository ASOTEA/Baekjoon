
def GCD(a, b):
    if b > 0 :
        r = a%b
        return GCD(b, r)
    else:
        return a

a, b = map(int, input().split())
k = int(GCD(a,b))

print(k)
print(int(a*b/k))    

