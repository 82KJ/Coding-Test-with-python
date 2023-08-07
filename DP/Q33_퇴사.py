# 1. 인풋 처리
n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

max_val = 0

# 2. DP 테이블 초기화 및 갱신 -> 점화식 = i~n까지 최대 이익
DP = [0]*(n+1)

for i in range(n-1,-1,-1):
    next_day = i + arr[i][0]
    
    if next_day <= n:
        DP[i] = max(arr[i][1] + DP[next_day], max_val)
        max_val = DP[i]
    else:
        DP[i] = max_val

print(DP[0])
