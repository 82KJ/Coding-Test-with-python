import heapq

# 1. 인풋 처리
n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

# 2. 다익스트라 적용
inf = int(1e9)
distances = [inf]*(n+1)
distances[1] = 0

q = list()
heapq.heappush(q, (0, 1))
while q:
  dist, now = heapq.heappop(q)

  if dist > distances[now]: continue

  for i in graph[now]:
    cost = dist + 1
    if cost < distances[i]:
      distances[i] = cost
      heapq.heappush(q, (cost, i))

# 3. 결과 출력 (번호, 거리, 같은 거리 개수)
res1 = 0
res2 = max(distances[2:])
res3 = 0
flag = False
for i in range(2, n+1):
  if flag == False and distances[i] == res2:
    res1 = i
    res3 += 1
    flag = True
  elif flag == True and distances[i] == res2:
    res3 += 1

print(res1, res2, res3)
    
  