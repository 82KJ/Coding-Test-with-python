from itertools import permutations

def solution(n, weak, dist):
    
    answer = len(dist) + 1
    
    length = len(weak)
    
    # 1. 원을 일자로 펴주기 위해 길이를 2배를 해준다
    for i in range(0,length):
        weak.append(weak[i] + n)
    
    # 2. 모든 취약점을 시작점으로 하여 계산을 수행한다
    for start in range(0, length):
        
        # 3. 시작점에 대하여 dist의 순열을 하나씩 적용한다
        for case in list(permutations(dist, len(dist))):
            cnt = 1 # 투입한 인원
            # 도착 위치 = 시작점 + dist
            position = weak[start] + case[cnt-1]
            
            # 시작점으로부터 모든 취약점을 순회하는 동안
            for index in range(start, start + length):
                # 아직 모든 취약점이 커버가 안되었으면, 
                if position < weak[index]:
                    cnt += 1 # 인원 추가
                    if cnt > len(dist):
                        break
                    position = weak[index] + case[cnt-1]
                
            answer = min(answer, cnt)
                    
    # 4. 예외처리: 만약, answer이 dist의 길이보다 크면 -1
    if answer > len(dist) : return -1
    
    return answer