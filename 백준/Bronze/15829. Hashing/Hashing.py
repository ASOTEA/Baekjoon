count = int(input())
word = input()

result = []
for seq, i in enumerate(word):
    result.append((ord(i)-96)*31**seq)
    
print(sum(result)%1234567891)