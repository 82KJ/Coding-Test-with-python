from collections import deque

# 1. input 처리
n,m = map(int, input().split())

visited = list()
for i in range(n):
  visited.append(list(map(int, input())))

# 2. bfs 처리
def bfs(row, col):
  queue = deque([(row,col)])
  
  visited[row][col] = 1

  # 상,하,좌,우 이동
  dy = [-1, 1, 0, 0]
  dx = [0, 0, -1, 1]
  
  while queue:
    v = queue.popleft()
    y = v[0]
    x = v[1] 
    
    for idx in range(4):
      ny = y + dy[idx]
      nx = x + dx[idx]

      if ny < 0 or nx < 0 or ny >= n or nx >=m:
        continue

      if visited[ny][nx] == 0:
        queue.append((ny,nx))
        visited[ny][nx] = 1

# 3. 방문 여부 체크하면서 결과 카운팅
res = 0
for row in range(n):
  for col in range(m):
    if visited[row][col] == 0:
      res += 1
      bfs(row,col)

print(res)

