def solution(s):
    # 1. 최초 길이
    length = len(s)
    min_length = length
    
    # 2. 1부터 절반길이 까지 반복
    for i in range(1, length//2 + 1):
        res = ""
        sum = 1
        cur = s[0:i]
        
        # cur과 next를 비교하면서, 일치하는지 확인
        for j in range(i,length,i):
            next = s[j:j+i]
            if cur == next:
                sum += 1
            else:
                if sum != 1:
                    res += str(sum)
                res += cur
                sum = 1
            cur = next
        
        # 남은 문자열에 대한 처리
        if sum != 1:
            res += str(sum)
            res += cur
        else:
            res += next
        
        # 3. 최소 길이 결과 저장
        if len(res) < min_length:
            min_length = len(res)
        
    answer = min_length
    
    return answer