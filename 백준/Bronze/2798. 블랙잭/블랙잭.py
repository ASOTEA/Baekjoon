cnt, Sum = map(int, input().split())
cad_num = list(map(int, input().split()))

result = 0
for i in range(cnt):            # 0 ~ 9
    for j in range(i+1,cnt):      # 1 ~ 9
        for k in range(j+1,cnt):  # 2 ~ 9 
            if cad_num[i]+cad_num[j]+cad_num[k] >Sum:
                continue
            else:
                result = max(result, cad_num[i]+cad_num[j]+cad_num[k])
print(result)