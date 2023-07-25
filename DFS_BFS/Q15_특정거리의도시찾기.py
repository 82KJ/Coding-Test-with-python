from collections import deque

# 1. 인풋 처리
n,m,k,x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)

dist = [0]*(n+1)
visited = [False]*(n+1)

# 2. bfs 진행
cnt = 0
q = deque()
q.append((x,0))
visited[x] = True

while q:
  cur_pos, cur_cnt = q.popleft()

  for i in graph[cur_pos]:
    if visited[i] == False:
      q.append((i, cur_cnt+1))
      visited[i] = True
      dist[i] = cur_cnt+1

# 3. 최종 결과 출력
flag = True
for i in range(1,len(dist)):
  if dist[i] == k:
    print(i)
    flag = False

if flag == True:
  print(-1)
    
  