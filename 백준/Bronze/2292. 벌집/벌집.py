num = int(input())

n = 1
N_cnt = 1
while num > n:
    n += 6*N_cnt
    N_cnt += 1
print(N_cnt)
