a,b = map(str, input().split())
a_back = a[::-1]
b_back = b[::-1]

if a_back > b_back:
  print(a_back)
else:
  print(b_back)
