c = int(input())

for i in range(c):
  n = list(map(int, input().split()))
  n_avg = sum(n[1:])/n[0] #평균

high_avg_cnt = 0 # 평균을 넘는 학생 수
for i in n[1:]:
  if i > n_avg:
    high_avg_cnt += 1

new_avg = high_avg_cnt/n[0]*100
print({new_avg:.3f}%')
