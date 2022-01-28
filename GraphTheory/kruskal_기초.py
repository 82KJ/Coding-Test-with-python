def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b : parent[b] = a
    else : parent[a] = b

# ========================================
v,e = map(int, input().split())

parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

edges = []
for i in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost,a,b))

# 1. edges를 cost 기준 오름차순 정렬한다
edges.sort()

res = 0
for i in edges:
    cost, a, b = i
    # 2. 만약, 해당 간선이 같은 집합이 아니라면, union한다
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res += cost

print(res)
