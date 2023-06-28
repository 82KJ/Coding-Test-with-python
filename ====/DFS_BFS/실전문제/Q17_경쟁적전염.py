from collections import deque

n,k = map(int, input().split())

q = []
map_data = []

for i in range(n):
    data = list(map(int, input().split()))
    map_data.append(data)
    for j in range(n):
        if data[j] != 0:
            q.append((data[j], i, j))
q.sort()            

q = deque(q)
s, y, x = map(int, input().split())
visited = [[-1]*(n) for _ in range(n)]


def bfs():
    for x in q:
        a,b,c = x
        visited[b][c] = 0

    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    while q:
        now = q.popleft()
        virus, y_pos, x_pos = now

        if visited[y_pos][x_pos] == s: break

        for i in range(4):
            yy = y_pos + dy[i]
            xx = x_pos + dx[i]

            if yy < 0 or xx < 0 or yy >= n or xx >= n: continue
            if map_data[yy][xx] != 0: continue

            map_data[yy][xx] = virus
            visited[yy][xx] = visited[y_pos][x_pos] + 1
            q.append((virus, yy, xx))


bfs()
print(map_data[y-1][x-1])