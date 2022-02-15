from collections import deque

n,l,r = map(int, input().split())

map_data = []
for _ in range(n):
    map_data.append(list(map(int, input().split())))

def bfs(i,j,union):
    q = deque()
    q.append((i,j))
    visited[i][j] = union

    united = []
    united.append((i,j))

    cnt = 0
    people = 0

    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    while q:
        y, x = q.popleft()
        people += map_data[y][x]
        cnt += 1

        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]

            if yy < 0 or xx < 0 or yy >= n or xx >= n: continue
            if visited[yy][xx] != 0: continue

            if abs(map_data[yy][xx] - map_data[y][x])>= l and abs(map_data[yy][xx] - map_data[y][x]) <=r:
                visited[yy][xx] = union
                q.append((yy,xx))
                united.append((yy,xx))
    
    # 2. 평균값으로 map을 갱신한다
    for i,j in united:
        map_data[i][j] = people // cnt

res = 0

while True:
    union = 1
    visited = [[0]*(n) for _ in range(n)]
    # 1. bfs로 탐색하면서 연합의 개수 와 인구수를 파악한다
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                bfs(i,j, union)
                union += 1

    # 3. 아예 인구이동이 불가능한 경우 그냥 탈출한다
    if union == n*n + 1 : break
    res += 1            
   
print(res)

    






