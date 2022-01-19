from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])

    # 1. 현재 노드 방문
    visited[start] = True

    while queue:
        # 2. 큐에서 vertex하나 꺼내기
        v = queue.popleft()
        print(v, end = ' ')

        # 3. v와 인접한 모든 vertex를 방문처리
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
# 인접 리스트로 graph 표현
graph = [[],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
]

# 방문 정보
visited = [False]*9

bfs(graph,1,visited)