from bisect import bisect_left, bisect_right

def count_by_range(arr, left, right):
    l_idx = bisect_left(arr, left)
    r_idx = bisect_right(arr, right)
    
    return r_idx - l_idx
    

def solution(words, queries):
    answer = []
    
    # 1. word의 길이를 인덱스로하는 배열 생성
    arr = [[] for _ in range(10001)] # ? 접미 쿼리와 매칭 위한 배열
    reversed_arr = [[] for _ in range(10001)] # ? 접두 쿼리와 매칭 위한 배열
    
    for word in words:
        arr[len(word)].append(word)
        reversed_arr[len(word)].append(word[::-1])
    
    # 2. 이진 탐색을 위해 생성 배열 정렬
    for i in range(10001):
        arr[i].sort()
        reversed_arr[i].sort()
    
    # 3. 접두 쿼리, 접미 쿼리 구분하며, 이진탐색 진행
    for querie in queries:
        if querie[0] != '?': # 접미 쿼리 --> ex) fro??? => froaaa와 frozzz 사이에 해당하는 word의 개수 찾기
            res = count_by_range(arr[len(querie)], querie.replace('?', 'a'), querie.replace('?', 'z'))
        else: # 접두 쿼리
            res = count_by_range(reversed_arr[len(querie)], querie[::-1].replace('?', 'a'), querie[::-1].replace('?', 'z'))
        answer.append(res)
    
    
    return answer