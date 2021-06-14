n = int(input())
score = list(map(int, input().split()))
m = max(score)

new_score = []
for i in score:
  new_score.append(i/m*100)

new_score_avg = sum(new_score)/n
print(new_score_avg)
