from collections import deque

# 1. 인풋 처리
n,l,r = map(int, input().split())

graph = list()
for i in range(n):
  graph.append(list(map(int, input().split())))

# 탐색을 진행하며, 연합 형성
def bfs(graph, union, start_y, start_x, union_num):
  q = deque()
  q.append((start_y, start_x))
  union[start_y][start_x] = union_num

  dy = [-1,1,0,0]
  dx = [0,0,-1,1]
  
  res = list()
  res.append((start_y,start_x))
  sum = graph[start_y][start_x]
  
  while q:
    cur_y, cur_x = q.popleft()

    for i in range(4):
      ny = cur_y + dy[i]
      nx = cur_x + dx[i]

      if ny < 0 or nx < 0 or ny >= n or nx >= n: continue
      if union[ny][nx] != 0: continue

      if abs(graph[ny][nx] - graph[cur_y][cur_x]) >= l and abs(graph[ny][nx] - graph[cur_y][cur_x]) <= r:
        res.append((ny,nx))
        sum += graph[ny][nx]
        union[ny][nx] = union_num
        q.append((ny,nx))

  return res, sum
  
# 2. 연합 형성이 더 이상 반복하지 않을 때까지 반복
res = 0
while True:
  union = [[0]*n for _ in range(n)]
  cnt = 1
  for i in range(n):
    for j in range(n):
      if union[i][j] == 0:
        arr, sum_arr = bfs(graph, union, i, j, cnt) # 연합 형성 + 연합 리스트 받기

        for u in arr:  # 연합 순회하며, 인구 분배
          u_y,u_x = u
          graph[u_y][u_x] = int(sum_arr / len(arr))
        
        cnt += 1

  # 종료 조건 -> 연합 생성이 1도 없음
  if cnt == n*n + 1:
    print(res)
    break
  else:
    res += 1
        

