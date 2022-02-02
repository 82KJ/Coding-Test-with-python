import heapq

def solution(food_times, k):
    # 다 먹었는데, k가 남아있다면 -1 반환
    if sum(food_times) <= k:
        return -1

    # 시간이 적게 걸리는 음식을 추출하기 위해, heapq 사용
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
    
    sum_val = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 시간
    leng = len(food_times) # 남은 음식 개수

    # (사용한 시간 + (현재 시간 - 이전 시간) * 음식 개수)가 k 이하라면,
    while sum_val + ((q[0][0] - previous) * leng) <= k:
        now = heapq.heappop(q)[0]
        sum_val += (now - previous) * leng
        leng -= 1
        previous = now
    
    # 번호 기준 정렬
    res = sorted(q, key = lambda x:x[1])
    return res[(k-sum_val) % leng][1]
