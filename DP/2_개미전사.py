# 1. 인풋 처리
n = int(input())
arr = list(map(int, input().split()))

# 2. DP 테이블 초기화
dp = [0] * 101
dp[0] = arr[0]
dp[1] = max(arr[0],arr[1])

# 3. DP 테이블 갱신
for i in range(2, n):
  dp[i] = max(dp[i-1], dp[i-2]+arr[i])

print(dp[n-1])
