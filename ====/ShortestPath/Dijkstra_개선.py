import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

distance = [INF]*(n+1)

def dijkstra(start):
    # 1. 시작 노드에 대한 초기화
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0

    # 2. 우선순위 큐가 빌때까지
    while q:
        # 2-1. 큐에서 가장 거리가 가까운 노드 정보 추출
        dist, now = heapq.heappop(q)

        # 2-2. 만약, 이미 처리한 노드라면 무시
        if distance[now] < dist: continue

        # 2-3. 인접한 노드 확인 후 최단 거리 갱신
        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INF", end = ' ')
    else:
        print(distance[i], end = ' ')