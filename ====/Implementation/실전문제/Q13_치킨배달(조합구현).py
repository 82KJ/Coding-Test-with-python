n,m = map(int, input().split())

chicken = []
houses = []
for i in range(n):
    data = list(map(int, input().split()))

    for j in range(n):
        if data[j] == 2:
            chicken.append((i+1,j+1))
        elif data[j] == 1:
            houses.append((i+1,j+1))

combi = [0]*m
res = int(1e9)

def combination(idx, level):
    global res
    if level == m:
        sum = 0
        for house in houses:
            y,x = house
            dist = int(1e9)
            for chick in combi:
                yy, xx= chick
                dist = min(dist, abs(y- yy) + abs(x - xx))
            sum += dist
        res = min(res, sum)
    else:
        for i in range(idx, len(chicken)):
            combi[level] = chicken[i]
            combination(i+1, level+1)

combination(0,0)
print(res)

