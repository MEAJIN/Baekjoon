a = int(input())
b = input()             # 만약, b = int(input()) 으로 입력하고

print(a*int(b[2]))      # print(a*b[2]) 로 연산을 하게 되면 << TypeError: 'int' object is not subscriptable >> 에러 발생
print(a*int(b[1]))      # 왜?
print(a*int(b[0]))      # 'b = 정수'로 정의 되어 있으며 이는 list 또는 Array 가 아니기 때문에, 정수인덱스로 접근 하는 것이 불가능 하기 때문
print(a*int(b))         # 즉, [] 은 [문자열] 만 접근이 가능 하다는 말 
