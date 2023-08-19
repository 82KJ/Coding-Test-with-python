# 1. 인풋 처리
n = int(input())

t = list()
p = list()
for i in range(n):
  a,b = map(int, input().split())
  t.append(a)
  p.append(b)

# 2. dp 테이블 초기화
dp = [0]*(n+1)

# 3. dp 테이블 갱신 --> dp[i] = i~n일까지의 최대 수익
max_val = 0
for i in range(n-1, -1, -1):
  next_day = i + t[i]

  if next_day <= n:
    dp[i] = max(p[i] + dp[next_day], max_val)
    max_val = dp[i]
  else:
    dp[i] = max_val

# 4. 결과 출력
print(max(dp))