# sum 함수 이용
def solve(a):
    return sum(a)
    
# for문 이용
def solve(a):
    total = 0
    for x in a:
        total += x
    return total
  
  
# 예시
def sum_list(lst):
  result = 0
  for i in lst:
    result += i
  return result

a = [1,1,1]
print(sum_list(a))
