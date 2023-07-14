# 1. 인풋 처리
arr = list(map(int, input()))

# 2. 0과 1은 더하기, 나머지는 곱하기
res = 0
for x in arr:
  if x == 0 or x == 1 or res == 0 or res == 1:
    res += x
  else:
    res *= x

print(res)