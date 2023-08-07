# 1. 인풋 처리
n = int(input())
m = int(input())

INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    
    if graph[a][b] != INF: # 짧은 간선만 저장하기
        graph[a][b] = min(graph[a][b], c)
    else:
        graph[a][b] = c

# 2. graph 대각선 0 초기화
for i in range(n+1):
    for j in range(n+1):
        if i == j : graph[i][j] = 0

# 3. 플로이드 워셜 진행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 4. 결과 출력
for i in range(1,n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end= " ")
        else:
            print(graph[i][j], end=" ")
    print()    
    