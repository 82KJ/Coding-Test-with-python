from itertools import combinations

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

# 치킨을 m개 뽑는 조합 라이브러리 이용
candidates = list(combinations(chicken,m))

def get_sum(candidate):
    res = 0
    for house in houses:
        y,x = house
        dist = int(1e9)
        
        for chick in candidate:
            yy, xx = chick
            dist = min(dist, abs(y-yy) + abs(x - xx))
        res += dist
    
    return res

res = int(1e9)
for candidate in candidates:
    res = min(res, get_sum(candidate))
print(res)