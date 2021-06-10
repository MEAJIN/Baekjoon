a = int(input())
b = int(input())
c = int(input())
multi = str(a*b*c)

for i in range(10):
  multi_cnt = multi.count(str(i)) # count 함수의 괄호( ) 안에는 찾는 문자열을 입력해야 하기 때문에 str함수를 이용해서 0부터 9까지 숫자를 각각 문자열로 변환
  print(multi_cnt)

  # 
