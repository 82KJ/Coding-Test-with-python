from gettext import find


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b : parent[b] = a
    else : parent[a] = b

v, e = map(int, input().split())
parent = [0]*(v+1)

for i in range(1, v+1):
    parent[i] = i

cycle = False

for i in range(e):
    a,b = map(int, input().split())

    # 만약, 두 노드의 루트 노드가 동일하다면, 사이클이 있다는 것이다
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 동일하지 않다면, union연산을 수행한다
    else:
        union_parent(parent, a, b)

if cycle == True:
    print("사이클이 발생")
else:
    print("사이클 따위 없습니다")