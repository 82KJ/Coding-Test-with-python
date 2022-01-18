n = int(input())
direction = list(input().split())

x, y = 1,1

move_types = ['L', 'R', 'U', 'D']
dy = [-1,1,0,0]
dx = [0,0,-1,1]

for i in direction:
    for idx in range(4):
        if(i == move_types[idx]):
            yy = y + dy[idx]
            xx = x + dx[idx]
    if(yy < 1 or yy > n or xx < 1 or xx > n): continue
    x,y = xx, yy

print(x,y)