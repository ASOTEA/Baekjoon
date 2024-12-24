answer = []

while True:
    input_num = input()
    
    if input_num == "0":
        break


    if input_num == input_num[::-1]:
        answer.append('yes')
    else: 
        answer.append('no')
for _ in answer:
    print(_)