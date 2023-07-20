def check(answer):
    for data in answer:
        x,y,a = data
        
        if a == 0: # 기둥
            # 바닥 or 좌측 보 or 우측 보 or 기둥 위
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or[x,y-1,0] in answer:
                continue
            else:
                return False
        elif a == 1: # 보
            # 좌측 아래 기둥 or 우측 아래 기둥 or 양쪽에 보
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = []
    
    # 모든 frame 순회하면서, 설치,삭제 후 만족 여부 확인
    for frame in build_frame:
        x,y,a,b = frame
        
        if b == 1:     # 설치
            answer.append([x,y,a])
            
            if check(answer) == False:
                answer.remove([x,y,a])
        elif b == 0:    # 삭제
            answer.remove([x,y,a])
            
            if check(answer) == False:
                answer.append([x,y,a])
            
    return sorted(answer)