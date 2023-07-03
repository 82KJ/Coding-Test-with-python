# 1. 인풋 처리
n,m = map(int, input().split())

coins = list()
for i in range(n):
  coins.append(int(input()))

# 2. DP 테이블 초기화
INF = 999999999
dp = [INF] * 10001
for i in coins:
  dp[i] = 1

# 3. DP 테이블 갱신
for i in range(1, m+1):
  for coin in coins:
    if i - coin >= 0:
      dp[i] = min(dp[i], dp[i-coin]+1)

if dp[m] == INF: print(-1)
else: print(dp[m])
    
  