from collections import deque

n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

visited = [[0]*m for _ in range(n)]

def bfs():
    queue = deque()
    queue.append((0,0))
    # 1. 현재 노드 방문 처리
    visited[0][0] = 1

    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    while queue:
        # 2. 큐에서 하나 꺼내기
        y,x = queue.popleft()

        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]

            if(yy < 0 or xx < 0 or yy >=n or xx >=m): continue
            if(graph[yy][xx] == 0): continue

            # 3. 조건을 만족하는 인접한 노드 방문처리하고 queue에 추가하기
            if(visited[yy][xx] == 0):
                visited[yy][xx] = visited[y][x] + 1
                queue.append((yy,xx))

bfs()
print(visited[n-1][m-1])