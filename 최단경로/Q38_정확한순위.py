# 1. 인풋 처리
n,m = map(int, input().split())

inf = int(1e9)
graph = [[inf]*(n+1) for _ in range(n+1)]
for i in range(m):
  a,b = map(int, input().split())
  graph[a][b] = 1 

# 2. 대각선 0 처리
for i in range(n+1):
  graph[i][i] = 0

# 3. 플로이드 적용
for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 4. 모든 노드에 대해 도달 가능하거나, 자기 자신으로 도달하거나 개수 체크
res = 0
for i in range(1, n+1):
  cnt = 0
  for j in range(1, n+1):
    if graph[i][j] != inf or graph[j][i] != inf:
      cnt += 1
  if cnt == n:
    res += 1

print(res)
    
    