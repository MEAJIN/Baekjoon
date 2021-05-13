# 64ms
a, b = map(int, input().split())
print(a-b)

# 64ms
a, b = input().split()
print(int(a)-int(b))


# split 을 , 로 쓰면 백준에선 런타임에러가 뜬다.! 
# 백준에서만 안돌아간다.!
# a,b = input().split(',')
# print(int(a)-int(b))
