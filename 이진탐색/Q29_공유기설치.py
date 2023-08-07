# 1. 인풋 처리
n,c = map(int, input().split())
arr = list()
for i in range(n):
    arr.append(int(input()))
arr.sort()

# 2. 이진 탐색을 수행하며, gap 조절
min_gap = 1
max_gap = arr[-1] - arr[0]
res = 1
while min_gap <= max_gap:
    gap = (min_gap + max_gap) // 2
    
    # gap을 기준으로 순서대로 배치 시작
    val = arr[0]
    cnt = 1
    for i in range(1, n):
        if arr[i] >= val + gap:
            cnt += 1
            val = arr[i]
    
    # 배치 개수가 c 이상이면, gap을 증가
    if cnt >= c:
        min_gap = gap + 1
        res = gap
    else:
        max_gap = gap - 1

print(res)
            
    