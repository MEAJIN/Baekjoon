word = input().upper() #싹다 대문자로 치환
word_set = list(set(word)) #중복제거 후, 알파벳 나열

wsc_list = []
for i in word_set: #알파벳 마다 반복문 돌면서
  ws_cnt = word.count(i) #word의 알파벳 개수를 셈
  wsc_list.append(ws_cnt) #문자열로 리스트에 추가
  
if wsc_list.count(max(wsc_list)) >= 2: #wsc_list의 최대값이 중복되거나 여러개 이면
  print('?')
else:
  max_index = wsc_list.index(max(wsc_list)) #제일 많이 사용한 단어 위치 탐색
  print(word_set[max_index])
