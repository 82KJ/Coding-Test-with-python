# 1. 인풋 처리
n = int(input())
m = int(input())

inf = int(1e9)
graph = [[inf]*(n+1) for _ in range(n+1)]
for i in range(m):
  a,b,c = map(int, input().split())
  graph[a][b] = min(graph[a][b], c) # 경로가 같으면, 작은 값 삽입

# 2. 대각선 0 처리
for i in range(n+1):
  graph[i][i] = 0

# 3. 플로이드 알고리즘
for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 4. 출력
for i in range(1, n+1):
  for j in range(1, n+1):
    if graph[i][j] == inf: print(0, end=" ")
    else: print(graph[i][j], end=" ")
  print()

