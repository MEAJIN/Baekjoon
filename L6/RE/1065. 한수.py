n = int(input())

cnt = 0 #한수 개수 세야 하니까 초기값 지정
for i in range(1,n+1): # 1부터 입력받은 자연수 까지
  n_list = list(map(int, str(i))) # 자연수를 문자형으로 쪼갬
  if i < 100: # 1~99까지는 전부 한수여서 바로 카운트
    cnt += 1
  elif n_list[0]-n_list[1] == n_list[1]-n_list[2]: # 각 배열의 차수가 같으면 한수로 카운트함 -> 쪼갠 문자형을 여기에 
    cnt += 1
    
print(cnt)
