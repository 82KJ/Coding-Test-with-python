# 1. 인풋 처리
n,m = map(int, input().split())

INF = 999999999
graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(m):
  a,b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

x, k = map(int, input().split())

# 2. 대각선 0 처리
for i in range(n+1):
  for j in range(n+1):
    if i == j: graph[i][j] = 0
      
# 3. 플로이드 워셜
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 4. 결과 출력
if graph[1][k] == INF or graph[k][x] == INF:
  print(-1)
else:
  print(graph[1][k]+graph[k][x])