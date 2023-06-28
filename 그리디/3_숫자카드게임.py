n,m = map(int, input().split())

max_val = -1
for row_idx in range(n):
  temp = list(map(int, input().split()))
  min_val = min(temp)
  max_val = max(max_val, min_val)

print(max_val)