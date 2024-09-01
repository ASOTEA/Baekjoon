# N장 카트 1~N번까지
# 1 맨 위에 N번쨰 맨 밑에

# 카드 벌리기
# 카드 밑으로 옮기기


N = int(input())

lst = [i for i in range(1, N+1)]

value = []


for i in range(len(lst)):
    if len(lst) == 0:
        break
    value.append(lst.pop(0))
    if len(lst) == 0:
        break
    lst.append(lst.pop(0))


for i in value:
    print(i , end = ' ')