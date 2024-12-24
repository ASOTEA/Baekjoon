output_list =[]


while True:

    pice = list(map(int, input().split()))

    if pice.count(0) > 2:
        break
    pice = sorted(pice)

    if  pice[0]**2 +pice[1] **2 == pice[2]**2:
        output_list.append('right')
    else: 
        output_list.append('wrong')

for _ in output_list:
    print(_)
