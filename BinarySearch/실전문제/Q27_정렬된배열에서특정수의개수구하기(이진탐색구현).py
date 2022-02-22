n, x = map(int, input().split())
data = list(map(int, input().split()))

# 1. 정렬된 배열에서 목표한 값의 첫번째 위치 찾기
def first(data, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2

    # target과 mid가 일치해도, 맨 왼쪽 값이여먄 index 반환
    if data[mid] == target and (mid == 0 or data[mid-1] < target):
        return mid
    
    # target과 일치하면서 맨 왼쪽 값이 아닌 경우는 여기에 걸린다
    elif data[mid] >= target:
        return first(data, target, start, mid-1)
    
    else:
        return first(data, target, mid+1, end)

# 2. 정렬된 배열에서 목표한 값의 마지막 위치 앚기
def last(data, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2

    # target과 mid가 일치해도, 맨 오른쪽 값이여먄 index 반환
    if data[mid] == target and (mid == n-1 or data[mid+1] > target):
        return mid
    
    elif data[mid] > target:
        return last(data, target, start, mid-1)
    
    # target과 일치하면서 맨 오른쪽 값이 아닌 경우는 여기에 걸린다
    else:
        return last(data, target, mid+1, end)
    
a = first(data, x,0,n-1)
b = last(data,x,0,n-1)

if a == None:
    print(-1)
else:
    print(b-a+1)
