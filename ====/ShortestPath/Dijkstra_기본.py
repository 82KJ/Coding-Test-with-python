import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수
n,m = map(int, input().split())
# 시작 노드 번호
start = int(input())

# 그래프 형성 - 연결리스트
graph = [[] for i in range(n+1)]
# 방문 여부 리스트
visited = [False] * (n+1)
# 최단 거리 테이블
distance = [INF] * (n+1)

# 간선 정보 입력
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

# ==================================================
# 순차탐색하며 방문하지 않은 노드 중에서 가장 작은 값을 가지는 노드 반환
def get_smallest_node():
    min_val = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            index = i
    return index

# 다익스트라 알고리즘으로 로 최단 거리 추출
def dijkstra(start):
    # 1. 시작 노드에 대해 초기화
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]

    # 2. 나머지 n-1개 노드에 대해 반복
    for i in range(n-1):
        # 2-1. 가장 작은 노드 반환 후 방문
        now = get_smallest_node()
        visited[now] = True 

        # 2-2. 인접한 노드 중에 갱신 가능한 노드 찾고 변환
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INF", end = ' ')
    else:
        print(distance[i], end = ' ')


# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2