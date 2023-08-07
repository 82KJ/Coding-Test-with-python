# 1. 인풋 처리
a = input()
b = input()

len_a = len(a)
len_b = len(b)
 
# 2. DP 테이블 초기화
DP = [[0]*(len_a+1) for _ in range(len_b+1)]

for i in range(len_b+1):
    DP[i][0] = i
for j in range(len_a+1):
    DP[0][j] = j

# 3. DP 테이블 갱신
for i in range(1, len_b+1):
    for j in range(1, len_a+1):
        if a[j-1] == b[i-1]: # 문자가 일치
            DP[i][j] = DP[i-1][j-1]
        else: # 문자가 불일치
            DP[i][j] = min(DP[i-1][j-1]+1, DP[i-1][j]+1, DP[i][j-1]+1)

print(DP[len_b][len_a])