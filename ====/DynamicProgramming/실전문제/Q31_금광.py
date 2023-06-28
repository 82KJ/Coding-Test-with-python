t = int(input())
while t:
    n,m = map(int, input().split())

    temp = list(map(int, input().split()))
    map_data = []
    for i in range(0, len(temp)- m + 1, m):
        map_data.append(temp[i:i+m])

    dp = [[0]*(m) for _ in range(n)]
    for i in range(n):
        dp[i][0] = map_data[i][0]
    
    d = [-1, 0, 1]
    for i in range(1, m):
        for j in range(n):
            for k in range(3):
                prev = j + d[k]
                if prev >= 0 and prev < n:
                    dp[j][i] = max(dp[j][i], map_data[j][i] + dp[prev][i-1])

    res = -int(1e9)
    for i in range(n):
        res = max(res, dp[i][m-1])

    print(res)
    t -= 1