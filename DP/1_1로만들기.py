# 1. 인풋 처리
x = int(input())

# 2. DP 테이블 초기화
dp = [0] * 30001

# 3. DP 테이블 갱신
for i in range(2, x+1):
  # 1을 빼는 경우
  dp[i] = dp[i-1] + 1

  # 5 나누기
  if i % 5 == 0:
    dp[i] = min(dp[i], dp[i//5] + 1)
  # 3 나누기
  if i % 3 == 0:
    dp[i] = min(dp[i], dp[i//3] + 1)
  # 2 나누기
  if i % 2 == 0:
    dp[i] = min(dp[i], dp[i//2] + 1)

# 4. 최종 결과 출력
print(dp[x])