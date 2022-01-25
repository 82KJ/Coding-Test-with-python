n = int(input())

dp = [0] * (n+1)

# 점화식 => An = min(An-1, An//2, An//5, An//3) + 1
for i in range(2,n+1):
    dp[i] = dp[i-1] + 1

    if i % 5 == 0 :
        dp[i] = min(dp[i], dp[i//5] + 1)
    if i % 2 == 0 :
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0 :
        dp[i] = min(dp[i], dp[i//3] + 1)
    
print(dp[n])