import heapq
import sys

input = sys.stdin.readline

# 1. 인풋 처리
n,m,s = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
  a,b,c = map(int, input().split())
  graph[a].append((b,c))

INF = 999999999
distance = [INF] * (n+1)

# 2. 다익스트라 알고리즘
def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist: continue

    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

# 3. 결과 출력
dijkstra(s)
cnt = 0
max_val = -1
for i in range(1, n+1):
  if distance[i] != INF and distance[i] != 0:
    cnt +=1
  if max_val < distance[i]:
    max_val = distance[i]

print(cnt, max_val)