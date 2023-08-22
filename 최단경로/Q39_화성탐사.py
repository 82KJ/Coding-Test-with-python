import heapq

t = int(input())

for _ in range(t):
  # 1. 인풋 처리
  n = int(input())
  graph = list()
  for _ in range(n):
    graph.append(list(map(int, input().split())))

  # 2. 다익스트라 적용
  inf = int(1e9)
  distances = [[inf]*n for _ in range(n)]
  distances[0][0] = graph[0][0]
  q = list()
  heapq.heappush(q, (graph[0][0],(0,0)))

  dy = [0,0,1,-1]
  dx = [-1,1,0,0]
  while q:
    dist, now = heapq.heappop(q)
    now_y,now_x = now

    if dist > distances[now_y][now_x]: continue

    for i in range(4):
      ny = now_y + dy[i]                         
      nx = now_x + dx[i]

      if ny < 0 or nx < 0 or ny >= n or nx >= n : continue

      cost = dist + graph[ny][nx]
      if cost < distances[ny][nx]:
        distances[ny][nx] = cost
        heapq.heappush(q, (cost, (ny,nx)))

  # 3. 결과 출력
  print(distances[n-1][n-1])
    
  
  
                 