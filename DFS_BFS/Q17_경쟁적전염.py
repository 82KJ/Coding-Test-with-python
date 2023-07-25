from collections import deque

# 1. 인풋처리
n,m = map(int, input().split())

graph = list()
viruses = list()
for i in range(n):
  temp = list(map(int, input().split()))
  graph.append(temp)

  for j in range(n):
    if temp[j] != 0:
      viruses.append((temp[j],0,i,j))
viruses.sort()

s,x,y = map(int, input().split())

# 2. bfs로 전염 진행
q = deque(viruses)

dy = [-1,1,0,0]
dx = [0,0,-1,1]

while q:
  virus, cnt, cur_y, cur_x = q.popleft()

  if cnt == s: break

  for i in range(4):
    ny = cur_y + dy[i]
    nx = cur_x + dx[i]

    if ny < 0 or nx < 0 or ny >= n or nx >=n: continue
    if graph[ny][nx] != 0: continue

    graph[ny][nx] = virus
    q.append((virus, cnt + 1, ny, nx))

# 3. 결과 출력
print(graph[x-1][y-1])