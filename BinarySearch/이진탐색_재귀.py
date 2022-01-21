def binary_search(array, target, start, end):
    # 탈출 조건 . array의 원소가 존재하지 않을 때
    if start > end: return None

    mid = (start + end) // 2

    if target == array[mid] : return mid
    elif target > array[mid] : return binary_search(array,target,mid+1,end)
    elif target < array[mid] : return binary_search(array,target,start,mid-1)

print("원소의 개수와 target을 입력하시오 : ", end ='')
n, target = map(int, input().split())

print("원소 전체를 입력하시오 : ", end = '')
array = list(map(int, input().split()))

res = binary_search(array,target,0,n-1)
if res == None: print("target이 존재하지 않습니다")
else : print(f"{res+1}번째에 존재합니다")