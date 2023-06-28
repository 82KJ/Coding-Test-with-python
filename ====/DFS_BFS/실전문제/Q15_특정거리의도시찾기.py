from collections import deque

n,m,k,x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [-1]*(n+1)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 0

    while q:
        now = q.popleft()

        for next in graph[now]:
            if visited[next] == -1:
                visited[next] = visited[now] + 1
                q.append(next)

bfs(x)

res = []
for i in range(1, n+1):
    if visited[i] == k:
        res.append(i)

if len(res) == 0:
    print(-1)
else:
    for x in res:
        print(x)