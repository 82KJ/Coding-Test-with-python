import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n,m,c = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,d = map(int, input().split())
    graph[a].append((b,d))

distance = [INF] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]: continue

        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

visited_city = 0
time = 0

for i in range(1, n+1):
    if i == c: continue

    if distance[i] != INF: 
        visited_city+=1
        time = max(time, distance[i])

print(visited_city, time)