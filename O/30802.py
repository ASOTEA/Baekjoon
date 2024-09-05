# 티쳐츠 S, M, L , XL , XXL, XXXL  총 6가지 T장 묶음
# 펜 한종류                                 P장 묶음

N = int(input()) # 참가자 수
lst = list(map(int, input().split())) # 옷의 개수
T, P = map(int, input().split())

cnt = 0
for i in lst:
    a, b = divmod(i, T)
    
    cnt += a
    if b > 0:
        cnt += 1
    
print(cnt)
print(*divmod(N, P))
