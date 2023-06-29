from collections import deque

# 1. input 처리
n,m = map(int, input().split())

graph = list()
for i in range(n):
  graph.append(list(map(int, input())))

visited = [[0]*m for _ in range(n)]

# 2. bfs 진행
def bfs():
  queue = deque([(0,0)])
  visited[0][0] = 1

  dy = [-1,1,0,0]
  dx = [0,0,-1,1]

  while queue:
    v = queue.popleft()
    y = v[0]
    x = v[1]
    
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]

      if ny < 0 or nx < 0 or ny >= n or nx >=m: continue
      if graph[ny][nx] == 1 and visited[ny][nx] == 0:
        queue.append((ny,nx))
        visited[ny][nx] = visited[y][x] + 1

# 3. 탐색 진행
bfs()
print(visited[n-1][m-1])
  
