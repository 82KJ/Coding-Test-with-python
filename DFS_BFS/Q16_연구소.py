from itertools import combinations
from copy import deepcopy
from collections import deque

# 1. 인풋 처리
n,m = map(int, input().split())

graph = list()
blanks = list()
viruses = list()

for i in range(n):
  temp = list(map(int, input().split()))
  graph.append(temp)
  for j in range(m):
    if temp[j] == 0: blanks.append((i,j))
    elif temp[j] == 2: viruses.append((i,j))


def bfs(y,x,graph):
  dy = [-1,1,0,0]
  dx = [0,0,-1,1]

  q = deque()
  q.append((y,x))
  
  while q:
    cur_y, cur_x = q.popleft()

    for i in range(4):
      ny = cur_y + dy[i]
      nx = cur_x + dx[i]

      if ny < 0 or nx < 0 or ny >= n or nx >= m: continue

      if graph[ny][nx] == 0:  
        graph[ny][nx] = 2
        q.append((ny,nx))


# 2. 3개의 벽을 세우는 조합을 순회
res = -1
for case in list(combinations(blanks, 3)):
  copied_graph = deepcopy(graph)
  
  # 3. 벽 세우기
  for pos in case:
    y, x = pos
    copied_graph[y][x] = 1

  # 4. 바이러스 위치를 기점으로 bfs 진행
  for virus in viruses:
    virus_y, virus_x = virus
    bfs(virus_y, virus_x, copied_graph)

  # 5. 안전 구역 개수 세기
  cnt = 0
  for row in copied_graph:
    for element in row:
      if element == 0:
        cnt += 1
  res = max(res, cnt)

# 6. 결과 출력
print(res)
    
    
  