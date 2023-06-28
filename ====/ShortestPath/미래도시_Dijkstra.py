import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

x,k = map(int, input().split())

distance1 = [INF] * (n+1)
distance2 = [INF] * (n+1)

def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now] : continue

        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

dijkstra(1, distance1)
dijkstra(2, distance2)

if distance1[k] != INF and distance2[x] != INF:
    print(distance1[k] + distance2[x])
else:
    print(-1)
    
