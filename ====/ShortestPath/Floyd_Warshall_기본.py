INF = int(1e9)

# 노드,간선 개수
n = int(input())
m = int(input())

# 최단거리 리스트 생성 + 자기 자신으로 가는 방향은 0으로 초기화
graph = [[INF]*(n + 1) for _ in range(n+1)]
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

# 간선 정보 입력
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

# 플로이드 와샬 구현 (점화식 D(a->b) = min(D(a->b), D(a->k) + D(k->b)))
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과 출력
for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][b] == INF: print("INF", end = ' ')
            else: print(graph[a][b], end = ' ')
        print()
