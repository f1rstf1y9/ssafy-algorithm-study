N = input()
nums = [1 for i in range(10)]
cnt = 1
for i in N:
  if i == '9' and not nums[9] and nums[6]:
    i = 6
  elif i == '6' and not nums[6] and nums[9]:
    i = 9   
  i = int(i)
  if nums[i]:
    nums[i] -= 1
  else:
    cnt += 1
    nums[i] -= 1
    for n in range(10):
      nums[n] += 1
print(cnt)
