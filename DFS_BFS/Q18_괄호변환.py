def is_right(p):
    cnt = 0
    for x in p:
        if x == '(':
            cnt += 1
        else:
            cnt -= 1
        if  cnt < 0 : return False
    
    return True

def get_answer(p):
    # 1. 빈 문자열 반환
    if p == '': return ''
    
    # 2. 균형잡인 괄호 문자열 두개로 분리
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(': cnt += 1
        else : cnt -= 1
        
        if cnt == 0:
            u = p[:i+1]
            v = p[i+1:]
            break
    
    # 3. u가 올바른 괄호 문자열
    if is_right(u):
        u += get_answer(v)
        return u
    # 4. u가 올바르지 않은 괄호 문자열
    else: 
        temp = '('
        temp += get_answer(v)
        temp += ')'
        u = u[1:-1]
        for x in u:
            if x == ')':
                temp += '('
            else:
                temp += ')'
        return temp
    
def solution(p):
    return get_answer(p)