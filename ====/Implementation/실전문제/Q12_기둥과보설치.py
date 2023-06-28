def check(answer):
    for data in answer:
        x,y,a = data
        
        # 기둥인 경우
        if a == 0:
            # 바닥, 보, 기둥 위면 continue
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            else: 
                return False
        # 보인 경우
        if a == 1:
            # 한 쪽 끝이 기둥이거나, 양쪽 끝이 보이면 continue
            if ([x,y-1,0] in answer or [x+1,y-1,0] in answer) or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            else:
                return False
    
    return True
        


def solution(n, build_frame):
    answer = []
    
    for frame in build_frame:
        x,y,a,b = frame
        
        if b == 1:
            answer.append([x,y,a])
            
            if check(answer) == False:
                answer.remove([x,y,a])
        
        elif b == 0:
            answer.remove([x,y,a])
            
            if check(answer) == False:
                answer.append([x,y,a])
    
    return sorted(answer)