c_a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] #crotia_alphabet
word = input()

for i in c_a:
	word = word.replace(i,'*')

print(len(word))

#replace는 문자열 자체를 변경하지 않고 바뀐 결과를 반환한다.
#따라서, 바뀐 결과를 유지하고 싶다면 문자열이 저장된 변수에 재할당을 해야함.
