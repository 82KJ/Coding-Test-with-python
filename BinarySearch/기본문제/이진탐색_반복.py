def binary_search(array, target, start, end):
    # 이진 탐색의 종료 조건은 원소가 한개도 남지 않았을 때
    while start <= end:
        mid = (start + end) // 2
        
        if array[mid] == target : return mid
        elif array[mid] > target :
            end = mid - 1
        elif array[mid] < target :
            start = mid + 1
    
    return None
    
print("원소의 개수와 target을 입력하시오 : ", end ='')
n, target = map(int, input().split())

print("원소 전체를 입력하시오 : ", end = '')
array = list(map(int, input().split()))

res = binary_search(array,target,0,n-1)
if res == None: print("target이 존재하지 않습니다")
else : print(f"{res+1}번째에 존재합니다")

