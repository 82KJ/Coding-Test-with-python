# 퀵정렬은 pivot값을 기준으로 정렬을 수행한다 (pivot 왼쪽은 pivot보다 작고, 오른쪽 큼)
# 이 과정을 재귀적으로 반복한다

a = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    # 탈출 조건 - 리스트의 원소가 1개만 남음
    if start >= end: return

    pivot = start
    left = start+1
    right = end

    while left <= right:
        
        # 1. left는 pivot보다 큰 값을 찾는다
        while left <= end and array[left] <= array[pivot]:
            left += 1

        # 2. right는 pivot보다 작은 값을 찾는다
        while right > start and array[right] >= array[pivot]:
            right -= 1  
        
        # 만약 left와 right가 교차하면, pivot과 작은 값을 교체한다
        if left > right: 
            array[pivot],array[right] = array[right],array[pivot]
        # 교차하지 않았다면, left와 right를 교체한다
        else : 
            array[left],array[right] = array[right],array[left]
    
    # pivot을 중심으로 정렬이 완료되었으니, 이제 양쪽 리스트를 재귀적으로 호출한다
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(a,0,len(a)-1)
print(a)