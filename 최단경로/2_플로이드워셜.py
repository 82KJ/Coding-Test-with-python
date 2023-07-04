# 1. 인풋 처리
INF = 999999999
n = int(input())
m = int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
  a,b,c = map(int, input().split())
  graph[a][b] = c
  
# 2. 대각선 0 처리
for i in range(1, n+1):
  for j in range(1, n+1):
    if i == j : graph[i][j] = 0

# 3. 플로이드 워셜 진행
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

print(graph)
