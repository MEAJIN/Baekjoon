A = int(input())
B = int(input())
C = int(input())

all_multiplication_str = str(A*B*C)

for i in range(10):
  all_multiplication_count = all_multiplication_str.count(str(i))
  print(all_multiplication_count)
