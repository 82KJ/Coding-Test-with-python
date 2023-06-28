n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int,input().split())))

dp = [[0]*n for _ in range(n)]
dp[0][0] = triangle[0][0]

for row in range(1,n):
    for col in range(row + 1):
        if col == 0:
            dp[row][col] = dp[row-1][col] + triangle[row][col]
        elif col == row:
            dp[row][col] = dp[row-1][col-1] + triangle[row][col]
        else:
            dp[row][col] = triangle[row][col] + max(dp[row-1][col-1], dp[row-1][col])

print(max(dp[n-1]))
