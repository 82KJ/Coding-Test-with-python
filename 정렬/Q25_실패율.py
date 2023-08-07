def solution(N, stages):
    answer = []
    
    # 1. 카운팅 배열 생성
    cnt_arr = [0]*(N+2)
    for stage in stages:
        cnt_arr[stage] += 1
        
    # 2. 실패율 구하기
    fail_rates = list()
    total_sum = sum(cnt_arr)
    
    for idx in range(1, N+1):
        if total_sum == 0:
            fail_rates.append((0,idx))
        else:
            fail_rates.append((cnt_arr[idx] / total_sum, idx)) 
            total_sum -= cnt_arr[idx]
            
    fail_rates.sort(key= lambda x: (-x[0], x[1]))

    # 3. idx를 answer로 옮기기
    for fail in fail_rates:
        answer.append(fail[1])
    
    return answer