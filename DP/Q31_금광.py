t = int(input())

for _ in range(t):
  # 1. 인풋 처리
  n,m = map(int, input().split())

  # 2. dp 테이블 초기화
  dp = [[0]*m for _ in range(n)]
  arr = list(map(int, input().split()))
  for i in range(n):
    for j in range(m):
      dp[i][j] = arr.pop(0)

  # 3. dp 테이블 갱신 -> MAX(DP[i-1][j-1], DP[i][j-1], DP[i+1],[j-1]) + 
  for j in range(1, m):
    for i in range(1, n):
      if i == 0:
        temp = max(dp[i][j-1], dp[i+1][j-1])
      elif i == n-1:
        temp = max(dp[i][j-1], dp[i-1][j-1])
      else:
        temp = max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])

      dp[i][j] = temp + dp[i][j]

  # 4. 결과 출력
  res = -1
  for i in range(n):
    res = max(res, dp[i][m-1])
  print(res)
    