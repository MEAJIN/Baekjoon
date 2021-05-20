#1
import sys
T = int(input())

for i in range(1,T+1):
  a,b = map(int,sys.stdin.readline().split())
  print('Case #%s:'%i,a+b)

#2
import sys
T = int(input())

for i in range(1,T+1):
  a,b = map(int,sys.stdin.readline().split())
  print('Case #%d: %d'%(i,a+b))
