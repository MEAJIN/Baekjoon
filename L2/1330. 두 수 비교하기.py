#1
a, b = map(int, input().split())

if a > b:
  print(">")
else:
  if a < b:
    print("<")
  else:
    print("=")

#2
a, b = map(int, input().split())

if a > b:
  print(">")
elif a < b:
  print("<")
else:
  print("==")
  
# 일화 : == 출력인데 = 라고 적어서 어이없게 4번이나 틀렸다.
#      : 난 진짜 문제좀 똑바로 읽어야 한다. 눈 좀 떠 임마!!
