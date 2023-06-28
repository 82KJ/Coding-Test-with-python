n = int(input())

res = 0
for hour in range(n+1):
  if '3' in str(hour):
    res += 3600
    continue
  for minute in range(60):
    if '3' in str(minute):
      res += 60
      continue
    for second in range(60):
      if '3' in str(second):
        res += 1
        continue
        
print(res)
      