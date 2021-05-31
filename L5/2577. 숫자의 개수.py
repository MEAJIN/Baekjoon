#1
A = int(input())
B = int(input())
C = int(input())

all_multiplication_str = str(A*B*C)

for i in range(10):
  all_multiplication_count = all_multiplication_str.count(str(i))
  print(all_multiplication_count)

#2
total = 1
for _ in range(3):
    i = int(input())
    total *= i  # 3개의 정수를 곱함
    
total_str = str(total)  # 숫자를 str타입으로 변환

for num in range(10):  # 0부터 9까지
    num_count = total_str.count(str(num))
    print(num_count)
