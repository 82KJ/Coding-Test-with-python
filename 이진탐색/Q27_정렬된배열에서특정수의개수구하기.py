# 1. 인풋 처리
n, x = map(int, input().split())
arr = list(map(int, input().split()))

# 2. 왼쪽 경계값 찾기
def get_left_boundary(arr, target, left, right):
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    # 중앙값과 일치하더라도, 왼쪽 끝값인지 확인 필요
    if arr[mid] == target and (mid == 0 or arr[mid-1] < target):
        return mid
    
    else:
        if arr[mid] < target:
            return get_left_boundary(arr, target, mid+1, right)
        elif arr[mid] >= target: # 중앙값과 일치해도, 왼쪽 끝값이 아닌 경우
            return get_left_boundary(arr, target, left, mid-1)
    

left_boundary = get_left_boundary(arr, x, 0, n-1)

# 3. 오른쪽 경계값 찾기
def get_right_boundary(arr, target, left, right):
        
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    # 중앙값과 일치하더라도, 오른쪽 끝값인지 확인 필요
    if arr[mid] == target and (mid == n-1 or arr[mid+1] > target):
        return mid
    
    else:
        if arr[mid] <= target: # 중앙값과 일치해도, 오른쪽 끝값이 아닌 경우
            return get_right_boundary(arr, target, mid+1, right)
        elif arr[mid] > target:
            return get_right_boundary(arr, target, left, mid-1)
    
right_boundary = get_right_boundary(arr, x, 0, n-1)


# 4. 결과 출력
if left_boundary == -1:
    print(-1)
else:
    print(right_boundary - left_boundary + 1)

