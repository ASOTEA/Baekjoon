num = int(input())
score = list(map(int, input().split()))
Max = max(score)

new_score = []

for i in score:
    new_score.append(i/Max*100)
score_avg = sum(new_score)/num
print(score_avg)