# 1. 인풋 처리
n = int(input())
arr = list(map(int, input().split()))

# 2. dp 테이블 초기화
dp = [1]*(n)

# 3. dp 테이블 갱신 -> dp[i] = i를 시작으로 최장 내림차순 수열 길이
for i in range(n-2, -1, -1):
  for j in range(i+1, n):
    if arr[i] > arr[j]: # 내림차순 성립
      dp[i] = max(dp[i], dp[j]+1)

# 4. 결과 출력
print(n-max(dp))
