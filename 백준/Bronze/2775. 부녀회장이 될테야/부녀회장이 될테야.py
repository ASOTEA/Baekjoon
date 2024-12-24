# Test case 를 제외한 나머지 부터 거들어 보기

T = int(input())
Test_case = []
result = []


for i in range(T*2):
    Test_case.append(int(input()))

for k in range(T):
    a = Test_case.pop(0)
    b = Test_case.pop(0)

    f1 = [1]
    f0 = [i+1 for i in range(b)]
    cnt = 0
    while cnt < a:
        for i in range(b-1):
            f1.append(f1[i]+f0[i+1])

        f0=f1
        f1 = [1]
        cnt += 1

    result.append(f0[-1])

for i in result:
    print(i)
