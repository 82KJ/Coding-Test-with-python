import heapq

t = int(input())

# 1. 테스트 케이스
for _ in range(t):
    # 2. 인풋 처리
    n = int(input())
    graph = list()
    for i in range(n):
        graph.append(list(map(int, input().split())))
                     
    INF = int(1e9)
    distance = [[INF]*(n) for _ in range(n)]

    # 3. 다익스트라 알고리즘 진행
    start = (graph[0][0], (0,0))
    q = list()
    heapq.heappush(q, start)
    
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    while q:
        cost, now = heapq.heappop(q)
        
        if distance[now[0]][now[1]] < cost: continue
        
        for i in range(4):
            ny = now[0] + dy[i]
            nx = now[1] + dx[i]
            
            if ny < 0 or nx < 0 or ny >= n or nx >= n: continue
            
            if cost + graph[ny][nx] < distance[ny][nx]:
                distance[ny][nx] = cost + graph[ny][nx]
                heapq.heappush(q, (distance[ny][nx], (ny,nx)))
                
    print(distance[n-1][n-1])