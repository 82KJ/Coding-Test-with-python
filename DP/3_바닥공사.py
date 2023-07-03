# 1. 인풋 처리
n = int(input())

# 2. DP 테이블 초기화
dp = [0] * 1001
dp[1] = 1
dp[2] = 3

# 3. DP 테이블 갱신
for i in range(3, n+1):
  dp[i] = (dp[i-1] + (dp[i-2]*2)) % 796796

print(dp[n])