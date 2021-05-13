# 1. 68ms
a, b = input().split()
print(int(a)+int(b))

# 2. 104ms
a, b = map(int, input().split()) # input으로 부터 값을 입력 받은 뒤, split 함수를 사용해 공백을 기준으로 입력 값을 나눈다.
print(a+b)                       # 그 후, map 함수를 사용해 입력 값을 int 형으로 변환

# map은 리스트의 요소를 지정된 함수로 처리한다.
# 보통 여러 개의 데이터를 한번에 다른 형태로 바꾸기 위해 사용한다.
