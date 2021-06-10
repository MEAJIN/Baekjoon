a = int(input())
b = int(input())
c = int(input())
multi = str(a*b*c)

for i in range(10):
  multi_cnt = multi.count(str(i))
  print(multi_cnt)
