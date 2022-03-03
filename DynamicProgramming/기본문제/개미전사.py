n = int(input())
array = list(map(int, input().split()))

dp = [0] * 1001

dp[0] = array[0]
dp[1] = max(dp[0], array[1])

# 점화식 A(i) = max(A(i-1), A(i-2) + a(i))
for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + array[i])

print(dp[n-1])

