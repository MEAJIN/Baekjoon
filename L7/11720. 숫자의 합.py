n = int(input())
nums = input()
nums_list = []

for i in range(n):
  nums_list.append(int(nums[i]))
  print(nums_list)
print(sum(nums_list))
