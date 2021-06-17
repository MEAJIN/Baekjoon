num = set(range(1,10001))

gen = set()
for i in range(1,10001):
  for j in str(i):
    i += int(j)
  gen.add(i)
    
s_n = sorted(num-gen)
for i in s_n:
  print(i)
