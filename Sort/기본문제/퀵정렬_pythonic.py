# python의 장점을 살린 퀵정렬
# 단, 비교 연산의 횟수가 증가해서 비효율적

a = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if(len(array) <= 1):
        return array
    
    # pivot을 index가 아닌 실제 값으로 지정
    pivot = array[0]
    tail = array[1:]

    # pivot을 중심으로 직접 비교 연산을 수행하여 partition 진행
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(a))