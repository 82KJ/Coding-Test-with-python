t = int(input())

# 1. 테스트 케이스 반복
for _ in range(t):
    
    # 2. 인풋 처리
    n,m = map(int, input().split())
    temp = list(map(int, input().split()))
    
    arr = [[0]*(m) for _ in range(n)]
    for idx, x in enumerate(temp):
        row = idx // m
        col = idx % m
        arr[row][col] = x
    
    # 3. DP 테이블 초기화
    DP = [[0]*(m) for _ in range(n)]
    for i in range(n):
        DP[i][0] = arr[i][0]
    
    # 4. DP 테이블 갱신
    for j in range(1,m):
        for i in range(n):
            if i == 0: # 0행
                temp = max(DP[i][j-1], DP[i+1][j-1])
            elif i == n-1: # 마지막행
                temp = max(DP[i][j-1], DP[i-1][j-1])
            else: # 나머지행
                temp = max(DP[i][j-1], DP[i+1][j-1])
                temp = max(temp, DP[i-1][j-1])
            DP[i][j] = temp + arr[i][j]
    
    # 마지막 열중 최대값 출력
    res = 0
    for i in range(n):
        res = max(res, DP[i][m-1])
    print(res)