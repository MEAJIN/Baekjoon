N = input()
save = N
count = 0

if (int(N)<10):
  N = '0'+N
  
while 1:
  ten = N[0]
  won = N[1]
  sum = (int(ten)+int(won))%10
  N = won+str(sum)
  
  count += 1

  if int(save) == int(N):
    print(count)
    break
