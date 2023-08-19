# 1. 인풋 처리
a = input()
b = input()

# 2. dp 테이블 초기화
dp =[[0]*(len(a)+1) for _ in range(len(b)+1)]
for i in range(len(a)+1):
  dp[0][i] = i
for i in range(len(b)+1):
  dp[i][0] = i

# 3. dp 테이블 갱신 (대각 아래: 교체, 일치 // 오른: 삭제 // 아래: 삽입)
for i in range(1, len(b)+1):
  for j in range(1, len(a)+1):
    if a[j-1] == b[i-1]:
      dp[i][j] = min(dp[i-1][j-1], dp[i-1][j] + 1, dp[i][j-1] + 1)
    else:
      dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j] + 1, dp[i][j-1] + 1)

# 4. 결과 출력
print(dp[len(b)][len(a)])