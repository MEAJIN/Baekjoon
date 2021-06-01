N = int(input())
test_score = list(map(int, input().split()))
max_test_score = max(test_score)

new_test_score = []
for i in test_score:
  new_test_score.append(i/max_test_score*100)

test_avg = sum(new_test_score)/N
print(test_avg)
