n,m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

dp = [99999] * 10001
dp[0] = 0

# 점화식 A(i) = min(A(i), A(i-k) + 1)
# for i in range(n):
#     for j in range(array[n], m+1):
#         dp[j] = min(dp[j], dp[j - array[i]]+1)

for i in range(1,m+1):
    for j in array:
        if i - j < 0: continue
        dp[i] = min(dp[i], dp[i-j]+1)

if dp[m] == 99999:
    print(-1)
else:
    print(dp[m])