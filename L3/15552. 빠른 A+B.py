# 조건 : input 대신 sys.stdin.readline을 사용

import sys

T = int(sys.stdin.readline()) # TEST CASE

for i in range(T):
  a, b = map(int, sys.stdin.readline().split())
  print(a+b)
  
  # TEST CASE 의 경우 input 을 사용해도 무방
  # 단, 반복문으로 여러줄 입력받는 상황에서는 반드시 sys.stdin.readline 을 사용
  
  # 한 개의 정수를 입력 받을 때 : a = int(sys.stdin.readline())
  # 정해진 개수의 정수를 한줄에 입력받을 때 : a,b,c = map(int,sys.stdin.readline().split())
  # 임의의 개수의 정수를 한줄에 입력받아 리스트에 저장할 때 : data = list(map(int,sys.stdin.readline().split()))
  # 임의의 개수의 정수를 n줄 입력받아 2차원 리스트에 저장할 때 :  data = []
  #                                                           n = int(sys.stdin.readline())
  #                                                           for i in range(n):
  #                                                           data.append(list(map(int,sys.stdin.readline().split())))
  # 문자열 n줄을 입력받아 리스트에 저장할 때 : n = int(sys.stdin.readline())
  #                                         data = [sys.stdin.readline().strip() for i in range(n)]
  
  
  # map()은 반복 가능한 객체(리스트 등)에 대해 각각의 요소들을 지정된 함수로 처리해주는 함수입니다.
  #위와 같이 사용한다면 a,b,c에 대해 각각 int형으로 형변환을 할 수 있습니다.  

  #list()는 자료형을 리스트형으로 변환해주는 함수입니다.
