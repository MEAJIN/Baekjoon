num = set(range(1,10001))

n_gen = set()
for i in range(1,10001):
  for j in str(i):
    i += int(j)
  n_gen.add(i)  # 집합 자료형에 값을 추가할 땐 'add' 를 잊지말자 제발 !

n_self = sorted(num-n_gen)
for i in n_self:
  print(i)
