c = int(input())

for _ in range(c):
  N = list(map(int, input().split()))
  N_avg = sum(N[1:])/N[0]

  N_high_avg_count = 0 
  for score in N[1:]:
    if score > N_avg:
      N_high_avg_count+= 1 # 평균보다 점수가 높은 학생 수

  N_proportion = N_high_avg_count/N[0]*100 # 평균을 넘는 학생들의 비율
  print(f'{N_proportion:.3f}%') # f'{}' 중 f는 접두사, {}는 변수나 계산식 사용을 위함
                                # 문자 = s, 정수 = d, 실수 = f
  
 
  # 출력은 f-string 사용 (https://ooyoung.tistory.com/87 참고)
