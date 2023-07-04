import heapq
import sys
input = sys.stdin.readline
INF = 999999999

# 1. 인풋 처리
n,m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
  a,b,c = map(int, input().split())
  graph[a].append((b,c))

# 2. 다익스트라 함수 구현
def dijkstra(start):
  q = []
  heapq.heappush(q, (0,start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q) # 가장 최단 거리 노드 추출

    if distance[now] < dist:
      continue # 이미 처리된 노드라면 무시 -> 방문 여부를 거리 비교로 확인

    # 현재 노드와 연결된 인접 노드를 확인해서 갱신
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]: # 구한 값이 기존 거리 보다 짧으면 갱신 진행
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

# 3. 다익스트라 진행
dijkstra(start)
print(distance)