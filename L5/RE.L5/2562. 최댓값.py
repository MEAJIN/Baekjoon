nums = []
for i in range(9):
  nums.append(int(input()))
  max_num = max(nums)
  
print(max_num)
print(nums.index(max_num)+1)
