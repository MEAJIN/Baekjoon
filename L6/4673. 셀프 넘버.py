num = set(range(1,10001)) # 1~10000 까지의 자연수

gen_num = set() # 생성자
for i in range(1,10001): # 1~10000 까지 반복문 돌리기
  for j in str(i):   # 1~10000 까지의 수를 문자열로 각각 쪼갬
    i += int(j)      # 쪼갠 값을 더함 ex) 123+1+2+3 => i = 128 
  gen_num.add(i)     # 더한 값을 생성자 변수에 삽입

self_num = sorted(num-gen_num) # 셀프넘버 추출 후 오름차순 정렬
for i in self_num:
  print(i)
