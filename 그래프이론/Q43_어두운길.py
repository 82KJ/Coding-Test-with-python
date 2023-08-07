# 1. 인풋 처리
n,m = map(int, input().split())

edges = list()
for i in range(m):
    a,b,c = map(int, input().split())
    edges.append((c,a,b))
edges.sort()

# 2. union&find 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b : parent[b] = a
    else: parent[a] = b

# 3. edges 순회하면서, cycle 생기면 추가 x
parent = [i for i in range(n+1)]
res = 0
for edge in edges:
    c,a,b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
    else:
        res += c

print(res)