#1
n = int(input())
nums = input()
nums_list = []

for i in range(n):
  nums_list.append(int(nums[i]))

print(sum(nums_list))

#2
n = int(input())

print(sum(map(int,input())))

#3
n = input()
nums = input()
total = 0
for i in nums :
    total += int(i)  # total= total+int(i)
print(total)
