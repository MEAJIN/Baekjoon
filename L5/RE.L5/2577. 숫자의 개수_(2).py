num = 1
for i in range(3):
  i = int(input())
  num *= i
  num_str = str(num)

for i in range(10):
  num_cnt = num_str.count(str(i))
  print(num_cnt)
