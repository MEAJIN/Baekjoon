word = input().upper()
word_list = list(set(word))

cnt_wlist = []
for i in word_list:
  cnt = word.count(i)
  cnt_wlist.append(cnt)

if cnt_wlist.count(max(cnt_wlist)) > 1: # if는 >= 2 로 대체 가능
  print('?')
else:                                                   # else는
  print(word_list[cnt_wlist.index(max(cnt_wlist))])     # max_index = cnt_wlist.index(max(cnt_wlist))
                                                        # print(word_list[max_index]) 로 대체 가능
#상단  
'''
● word : 단어
→ 대/소문자 구분 없으니 upper() 함수를 사용하여 전부 대문자로 치환
→ apple 을 입력하면 APPLE 로 치환

● word_list : 중복값이 제거 된 단어(알파벳)
→ ['A','P','L','E']
→ 중복 제거 후, 알파벳이 나열 되는 순서는 랜덤
'''

#중단(for문)
'''
● for i in word_list:
→ 나열 된 각각의 알파벳을 for문으로 반복

● cnt : 각각의 알파벳 개수
→ word 의 단어를 셈

● cnt_wlist : cnt를 리스트에 각각 추가
→ 추가 되는 순서는 word_list 원소의 순서와 동일 (for문이 word_list 나열 순으로 돌아가기 때문)
→ [1,2,1,1]
'''

#하단(if-else문)
'''
[if]
● cnt_wlist.count(max(cnt_wlist)) > 1:
→ cnt_wlist 리스트의 최대값(max) 개수가 1보다 많으면 '?' 를 출력 
→ 이는 가장 많이 사용 된 알파벳이 여러 개 존재할 경우를 뜻함 (아래 #출력조건 참고)

[else]
● print(word_list[cnt_wlist.index(max(cnt_wlist))])
  ● cnt_wlist.index(max(cnt_wlist))
  → index() 함수를 이용하여 cnt_wlist 리스트의 최대값 위치를 찾음
→ word_list 리스트와 cnt_wlist 리스트 에서 같은 인덱스에 위치한 문자열 출력
→ P  
'''

#출력조건
'''
첫째 줄에 이 단어(에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
'''
