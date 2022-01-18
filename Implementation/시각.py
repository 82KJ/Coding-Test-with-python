n = int(input())
cnt = 0

for h in range(0,n+1):
    for m in range(0,60):
        for s in range(0,60):
            time = str(h)+ str(m) + str(s)
            if '3' in time: cnt+=1
print(cnt)

# 완전탐색은 data가 100만개 이하면 사용