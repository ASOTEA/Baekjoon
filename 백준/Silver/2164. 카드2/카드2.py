n = int(input())

for i in range(19):
    if 2**i < n <= 2**(i+1):
        break
if (n == 1 or n== 2):
    print(n)
else:
    print((n - 2**i) *2)