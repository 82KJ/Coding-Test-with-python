import heapq

def solution(food_times, k):
    # 0. 예외처리
    if sum(food_times) <= k:
        return -1
    
    # 1. heapq에 (time, idx) 삽입
    q = []
    for idx,time in enumerate(food_times):
        heapq.heappush(q, (time,idx+1))
    
    # 2. 남은 음식 수 x pop 음식 다 먹는 시간이 k보다 작은지 체크
    previous = 0
    length = len(q)
    while (q[0][0] - previous) * length <= k:
        k -= (q[0][0] - previous) * length
        now = heapq.heappop(q)[0]
        length-=1
        previous = now
    
    # 3. 정렬 후, 알맞은 인덱스 출력
    q.sort(key=lambda x:x[1])
    return q[k%len(q)][1]
    