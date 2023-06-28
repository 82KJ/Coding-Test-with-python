n = int(input())
data = list(map(int, input().split()))
dp = [1]*n

# dp[i] = i번째 병사부터 마지막 병사까지 최장 내림차순 배열 길이
for i in range(n-2, -1, -1):
    for j in range(i,n):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))