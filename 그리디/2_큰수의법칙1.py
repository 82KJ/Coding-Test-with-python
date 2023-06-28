n,m,k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

first_large_num = nums[-1]
second_large_num = nums[-2]

res = 0
for i in range(m):
  if i != 0 and i % k == 0:
    res += second_large_num
  else:
    res += first_large_num

print(res)