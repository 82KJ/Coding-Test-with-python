from itertools import combinations
from collections import deque
from copy import deepcopy

n,m = map(int, input().split())

map_data = []

viruses = []
blanks = []
for i in range(n):
    data = list(map(int, input().split()))
    map_data.append(data)

    for j in range(m):
        if data[j] == 0:
            blanks.append((i,j))
        elif data[j] == 2:
            viruses.append((i,j))

wall = list(combinations(blanks, 3))

def bfs(map_data):
    q = deque()
    for x in viruses:
        q.append(x)
    
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    while q:
        now = q.popleft()
        y, x = now

        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]

            if yy < 0 or xx < 0 or yy >= n or xx >= m: continue
            if map_data[yy][xx] != 0: continue

            map_data[yy][xx] = 2
            q.append((yy,xx))

res = 0
for case in wall:
    temp_data = deepcopy(map_data)

    for x in case:
        a,b = x
        temp_data[a][b] = 1
    
    bfs(temp_data)
    cnt = 0
    for r in temp_data:
        for c in r:
            if c == 0:
                cnt += 1
    res = max(res, cnt)

print(res)

    
    