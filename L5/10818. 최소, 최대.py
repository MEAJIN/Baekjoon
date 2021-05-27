# 1번째 시도  -----> 런타임 에러 발생 ----> ㅋㅋ
N = int(input())

for i in range(N):
  num = list(map(int, input().split()))
  print(min(num),max(num))

# 2번째 시도 -> 답은 맞으나 :: 메모리 144968KB / 시간 444ms / 코드 길이 81B -> 실화냐?
N = int(input())
num = list(map(int, input().split()))

print(min(num),max(num))

# 3번째 시도 -> 답은 맞으나 :: 메모리 148932KB / 시간 444ms / 코드 길이 82B-> 왜 튜플이 리스트 보다 메모리를 더 먹지..?
N = int(input())
num = tuple(map(int, input().split()))

print(min(num),max(num))

# 4번째 시도 -> 답은 맞으나 :: 메모리 144968KB / 시간 444ms / 코드 길이 96B-> 2번째 시도랑 같은 결과가 나왔다.
N = int(input())
num = list(map(int, input().split()))

print('{} {}'.format(min(num),max(num)))

# 그냥 이 문제 자체가 메모리를 오지게 잡아 먹는 문제인가보다 (?)
## format은 문자열을 포매팅 해서 (이쁘게)재사용 하는 함수이다. >> 형식 : {인덱스0}, {인덱스1}'.format(값0, 값1)
### 파이썬은 배열에 값을 입력 받을 때 Test Case의 갯수와 상관이 없기 때문에 일단 입력만 받아 놓고 진행 한다.

