from itertools import permutations

def solution(n, weak, dist):
    answer = 999999999
    length = len(weak)
    
    # 1. 원형 데이터를 2배로 펼치기
    for i in range(length):
        weak.append(weak[i]+n)
    
    # 2. 모든 취약점 순회
    for start in range(length):
        
        # 3. 모든 거리 순열 순회
        for case in list(permutations(dist,len(dist))):
            cnt = 1
            position = weak[start] + case[cnt-1]
            
            # 4. 각 거리 순열마다 모든 취약점을 포함하는지 check
            for index in range(start, start+length):
                if position < weak[index]:
                    cnt += 1
                    if cnt > len(dist):
                        break # 만약 투입 인원이 전체 인원보다 많으면, 그냥 종료 
                    position = weak[index] + case[cnt-1]
            
            answer = min(answer, cnt)
            
    # 5. 예외처리
    if answer > len(dist): return -1
        
    return answer