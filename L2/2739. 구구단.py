#1
a = int(input())

for i in range(1,10):
    print(a, '*', i, '=', a*i)



#2 (백준식 정답은 아니지만 구구단은 맞음)
for i in range(2,3):
  for j in range(1,10):
    print(i, '*', j, '=', i*j)
    
    
   
# range(1) == 0
# ranger(1,2) == 1
# ranger(1,10) == 1~9 
