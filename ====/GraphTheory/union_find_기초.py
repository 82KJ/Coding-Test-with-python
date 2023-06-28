# 원소 x가 속한 집합을 찾는 함수
def find_parent(parent,x):
    # 만약, x의 부모가 자기 자신이 아니라면,
    # 재귀호출을 통해 부모를 타고 들어가 루트 노드를 찾는다
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치는 함수
def union_parent(parent, a, b):
    # 두 원소의 루트 노드를 찾아서 반환한다
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    # 값이 작은 노드를 부모 노드로 하기 때문에,
    # b가 더 크면 b의 부모를 a로 한다 (반대는 a의 부모를 b로한다)
    if a < b : parent[b] = a
    else : parent[a] = b

#==================================================================

# 정점, 간선의 개수 입력
v, e = map(int, input().split())

# 부모테이블 초기화
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

# union 연산 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent,a,b)

# 각 원소가 속한 집합 출력
print("각 원소가 속한 집합 : ", end = '')
for i in range(1, v+1):
    print(find_parent(parent, i), end= ' ')
print()

# 각 원소의 부모 출력
print("부모 테이블 : ", end = ' ')
for i in range(1,v+1):
    print(parent[i], end = ' ')
