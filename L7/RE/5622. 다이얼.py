dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word  = input()

sum = 0
for i in range(len(word)):
	for j in dial:
		if word[i] in j:
			sum += dial.index(j)+3

print(sum)

# if * in ** 를 사용 할 땐, *에 문자열이 와야한다. 
