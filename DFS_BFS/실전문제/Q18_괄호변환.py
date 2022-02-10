def is_right(text):
    stack = []
    for x in text:
        if x == '(':
            stack.append(x)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                return False
    if len(stack) == 0: return True
    else: return False

def get_string(text):
    # 1. 빈 문자열 처리
    if len(text) == 0: return text
    
    # 2. u와 v로 분리
    u = ''
    v = ''
    left_cnt, right_cnt = 0,0
    for i in range(0,len(text)):
        if text[i] == '(': left_cnt += 1
        else: right_cnt += 1
        
        if left_cnt == right_cnt :
            u = text[0:i+1]
            v = text[i+1:]
            break

    # 3. u가 올바른 괄호 문자열
    if is_right(u): 
        res = u + get_string(v)
    # 4. u가 올바른 괄호 문자열이 아님
    else:
        new_u = ''
        for x in u[1:-1]:
            if x == '(': new_u += ')'
            else: new_u += '('
                
        res = '('+ get_string(v) + ')'+new_u
        
    return res
    

def solution(p):
    answer = get_string(p)
    
    return answer