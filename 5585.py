N = int(input())


def joi(x):
    cnt = 0
    if x//500 >= 1:
        cnt += x//500
        x = x%500
    if x//100 >= 1:
        cnt += x//100
        x = x%100
    if x//50 >= 1:
        cnt += x//50
        x = x%50
    if x//10 >=1:
        cnt += x//10
        x = x%10
    if x//5 >= 1:
        cnt += x//5
        x = x%5
    if x//1 >= 1:
        cnt += x//1

    return print(cnt)

joi(1000-N)