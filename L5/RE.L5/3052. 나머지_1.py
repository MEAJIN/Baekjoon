nums = []
for i in range(10):
  i = int(input())
  nums.append(i%42)
  nums_re = set(nums)
print(len(nums_re))
