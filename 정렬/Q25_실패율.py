def solution(N, stages):
    answer = []
    
    # 1. 카운팅 배열 생성
    cnt_arr = [0] * (N+2)
    for s in stages:
        cnt_arr[s] += 1
    
    # 2. 실패율 구하기
    fail_rate = list()
    leng = len(stages)
    for i in range(1,N+1):
        if leng == 0:
            fail_rate.append((0, i))
        else:
            fail_rate.append((cnt_arr[i]/leng, i))
            leng -= cnt_arr[i]
    
    # 3. 실패율 정렬
    fail_rate.sort(key=lambda x : (-x[0],x[1]))
    
    for f in fail_rate:
        a,b = f
        answer.append(b)
    
    return answer