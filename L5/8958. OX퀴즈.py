N = int(input())

for _ in range(N):
  quiz_list = list(input())
  
  quiz_score = 0
  total_quiz_score = 0
  for check in quiz_list:
    if check == 'O':
      quiz_score += 1
      total_quiz_score += quiz_score
    else:
      quiz_score = 0

  print(total_quiz_score)
