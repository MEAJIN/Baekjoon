#1
n = int(input())
cnt = 1
cnt_six = 6
count = 1
while n > cnt:
    count += 1
    cnt += cnt_six
    cnt_six += 6
print(count)

#2
N = int(input())
first = 1
plus = 6
room = 1

if N == 1:
    print(1)
else:
    while True:
        first = first + plus
        room+= 1
        
        if N <= first:
            print(room)
            break
        plus += 6
