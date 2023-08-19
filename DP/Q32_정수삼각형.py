# 1. 인풋 처리
n = int(input())
dp = list()
for i in range(n):
  dp.append(list(map(int, input().split())))

# 2. dp 테이블 초기화 -> 0열, 마지막열
for i in range(1,n):
  dp[i][0] += dp[i-1][0]
  dp[i][-1] += dp[i-1][-1]

# 3. dp 테이블 갱신
for i in range(2,n):
  for j in range(1,i):
    dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + dp[i][j]

# 4. 결과 출력
print(max(dp[n-1]))
    