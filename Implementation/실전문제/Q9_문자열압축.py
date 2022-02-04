# 같은 문자열이 연속하여 나오는지 체킹하는 방법은 어느정도 형태를 외워두자
# now와 next를 구분하고 이후 now를 next로 계속 치환해준다

def solution(s):
    answer = len(s)

    max_iter = len(s)//2
    for step in range(1, max_iter+1):
        now = s[0:step]

        cnt = 1
        compressed = ''
        for j in range(step, len(s), step):
            next = s[j:j+step]

            if now == next:
                cnt += 1
            else:
                compressed += str(cnt) + now if cnt >= 2 else now
                cnt = 1
                now = next
        
        compressed += str(cnt) + now if cnt >= 2 else now

        answer = min(answer, len(compressed))
    
    return answer

