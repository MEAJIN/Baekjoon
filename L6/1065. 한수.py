def hansu(n):
  hansu_cnt = 0
  for i in range(1,n+1):
    n_list = list(map(int,str(i)))
    
    if i < 100: #100보다 작은 수는 모두 한수
      hansu_cnt += 1 
    elif n_list[0]-n_list[1] == n_list[1]-n_list[2]: #  배열의 차이가 같으면 한수
      hansu_cnt += 1
  
  return hansu_cnt

n = int(input())
print(hansu(n))


#어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
