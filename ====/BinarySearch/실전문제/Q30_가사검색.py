from bisect import bisect_left, bisect_right

def count_by_range(array, l_value, r_value):
    l_idx = bisect_left(array,l_value)
    r_idx = bisect_right(array,r_value)
    return r_idx - l_idx
    
def solution(words, queries):
    answer = []
    array = [[] for _ in range(10001)]
    reversed_array = [[] for _ in range(10001)]

    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])
    
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()
        
    for q in queries:
        if q[0] != '?':
            res = count_by_range(array[len(q)], q.replace('?','a'), q.replace('?','z'))
        else:
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?','a'), q[::-1].replace('?','z'))
        
        answer.append(res)
    
    return answer