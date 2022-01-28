# 원소 x의 루트 노드를 반환하는 함수
def find_parent(parent,x):
    # 부모가 자기 자신이 아닐 경우, 재귀적으로 함수를 호출하여
    # 부모 노드를 계속 갱신한다. 최종적으로 부모노드를 루트노드로 만든다
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

# 원소 a,b가 속한 집합을 합집합하는 함수
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    # 큰 루트 노드의 부모를 작은 루트 노드로 갱신한다
    if a < b : parent[b] = a
    else : parent[a] = b

# ==================================================================
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

# 각 원소의 부모 출력 => union 이후 find가 아직 실행 안됨 => 경로 압축 x
print("부모 테이블 : ", end = ' ')
for i in range(1,v+1):
    print(parent[i], end = ' ')
print()

# 각 원소가 속한 집합 출력 => find가 실행되면서 경로 압축 o
print("각 원소가 속한 집합 : ", end = '')
for i in range(1, v+1):
    print(find_parent(parent, i), end= ' ')
print()

# 각 원소의 부모 출력 => 이제 같은 집합인지 확인 하기 위해서, find를 하는게 아니라 parent만 확인하면 된다
print("부모 테이블 : ", end = ' ')
for i in range(1,v+1):
    print(parent[i], end = ' ')