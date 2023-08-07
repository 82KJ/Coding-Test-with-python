# 1. 인풋 처리
n,m = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    temp = list(map(int, input().split()))
    for j in range(1,n+1):
        graph[i][j] = temp[j-1]

travel_plans = list(map(int, input().split()))
parents = [i for _ in range(n+1)]

# 2. union&find 함수
def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    
    if a < b: parents[b] = a
    else : parents[a] = b

# 3. graph 순회하면서 union 진행
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == 1:
            union_parent(parents, i, j)

# 4. 여행 계획이 모두 같은 parent를 가지는지 확인
flag = True
pp = find_parent(parents, travel_plans[0])
for i in range(1, len(travel_plans)):
    cp = find_parent(parents, travel_plans[i])
    
    if pp != cp:
        flag = False

if flag == True: print("YES")
else : print("NO")
    