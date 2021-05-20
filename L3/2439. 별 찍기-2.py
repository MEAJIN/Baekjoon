# 이게 정답
T = int(input())

for i in range(1, T+1):
    print(' '*(T-i)+'*'*i)
    
    
    
# 삽질 하다가 신기한 삼각형을 뽑았다

T = int(input())

for i in range(0,T+1):
    print('*'*(T-i),'*'*i)
    
 # 이걸 출력해보면 
      ***** 
      **** *
      *** **
      ** ***
      * ****
       *****           
 # 이렇게 나온다 ㅋㅋ
