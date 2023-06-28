n = int(input())
t = []
p = []

for i in range(n):
    a,b = map(int, input().split())
    t.append(a)
    p.append(b)

# dp[i] = i번째 날부터 마지막 날가지 낼 수 있는 최대 이익
dp = [0]*(n+1)
max_val = 0

for i in range(n-1, -1, -1):
    time = t[i] + i

    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        dp[i] = max(p[i] + dp[time], max_val)
        max_val = dp[i]
    # 상담이 기간을 벗어나는 경우 
    else:
        dp[i] = max_val

print(max_val)



    



        