n,c = map(int, input().split())

data = []
for _ in range(n):
    data.append(int(input()))
data.sort()

res = 0
def binary_search(data, start, end):
    global res
    if start > end:
        return res
    
    # 가장 인접한 두 공유기 사이의 거리
    gap = (start + end) // 2

    # 1. gap을 기준으로 공유기 배치 시작
    cnt = 1 # data[0]은 이미 배치
    val = data[0]
    for i in range(1,n):
        if data[i] >= val + gap:
            cnt += 1
            val = data[i]
    
    # 2. 만약 공유기 배치가 전부 이뤄지면,
    if cnt >= c:
        res = gap # 현재 최적의 결과를 지정
        return binary_search(data, gap+1, end)
    # 3. 만약 공유기 배치를 모두 실패하면,
    else:
        return binary_search(data, start, gap-1)

print(binary_search(data, 1, data[-1] - data[0]))