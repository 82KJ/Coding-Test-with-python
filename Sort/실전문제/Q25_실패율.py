def solution(N, stages):
    people = len(stages)
    
    fail_data = []
    for i in range(1,N+1):
        # 해당 스테이지의 사람 수 count
        cnt = stages.count(i)
        
        # 실패율 계산
        if people != 0:
            fail = cnt / people
        else:
            fail = 0.0
        
        fail_data.append((fail,i))
        people -= cnt

    # 내림차순 정렬
    fail_data.sort(key=lambda x:(-x[0],x[1]))
    
    answer = [x[1] for x in fail_data]
    
    return answer