def dfs(graph, v, visited):
    # 1. 현재 노드 방문 처리
    visited[v] = True
    print(v, end = ' ')

    # 2. 현재 노드와 연결된 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

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

dfs(graph, 1, visited)