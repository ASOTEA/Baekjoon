
# 같은 눈 4개 50,000 + 같은눈 *5,000
    # (a,a,a,a) 50,000 + 5000*a

# 같은 눈 3개 10,000 + 3개가 나온눈 *1,000
   # (a,a,a,b) 10,000 + 1000*a

# 같은 눈 2개씩 두쌍 + 2,000원+(2개가 나온 눈)×500원+(또 다른 2개가 나온 눈)×500
    # (a,a,b,b) 2000+500*(a+ b)

# 같은 눈 2개만 나오는 경우1,000원+(같은 눈)×100
    # (a,a,b,c) 1,000 + 100*a

# 모두 다른 눈이 나오는 경우 가장큰 눈 x 100
    # max(a,b,c,d)*100

def func(lst):
    if len(set(lst)) == 1:
        return 50000 + lst[0] * 5000
    if len(set(lst)) == 2:
        if lst[1] == lst[2]:
            return 10000 + lst[1] * 1000
        else:
            return 2000 + lst[0] * 500 + lst[2] * 500
    for i in range(3):
        if lst[i] == lst[i+1]:
            return 1000 + lst[i] * 100
    return lst[3] * 100

N = int(input())
max_lst = []
for _ in range(N):
    lst = sorted(list(map(int, input().split())))
    max_lst.append(func(lst))
print(max(max_lst))