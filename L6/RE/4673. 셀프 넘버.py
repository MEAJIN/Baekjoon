num = set(range(1,10001))

gen = set() # 생성자
for i in range(1,10001):
  for j in str(i): # 값 쪼개기
    i += int(j) # 쪼갠 값 더함
  gen.add(i)

self_n =  sorted(num-gen)
for i in self_n:
  print(i)
