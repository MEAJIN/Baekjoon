# 리스트 자료형으로 접근
num_list = []

for i in range(10):
  i = int(input())
  num_list.append(i%42)
num_list_remainder = set(num_list)  # 리스트 자료형인 num_list를 집합 자료형으로 변환

print(len(num_list_remainder)) # 자료형 이니 len 함수를 사용하여 집합의 개수를 셈


# 집합 자료형으로 접근
num_set = set()  # num_set의 중복 값을 제거

for i in range(10):
  i = int(input())
  num_set.add(i%42) # 자료형은 add 함수를 이용하여 집합에 요소를 추가한다. (리스트는 append 함수를 사용)

print(len(num_set)) 


## 집합(set) 자료형은, 집합에 관련된 것을 쉽게 처리하기 위해 만든 자료형이다. ==> 중복 요소를 제거, 순서가 없음
## 비어 있는 집합 자료형은 s = set()로 만들수 있다.
