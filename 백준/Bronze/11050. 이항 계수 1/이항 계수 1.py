n, k = map(int, input().split())

sum = 1
for i in range(n,0,-1):
    if i == n-k:
        break
    sum = sum*i

sum_1 = 1

for j in range(1, k+1):
      sum_1= j*sum_1

print(int(sum/sum_1))


