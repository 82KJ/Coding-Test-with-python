# 1. 선택 정렬 - 매번 가장 작은 것을 선택
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
  min_idx = i
  for j in range(i+1, len(array)):
    if array[min_idx] > array[j]:
      min_idx = j

  array[i],array[min_idx] = array[min_idx],array[i]

print(array)

# 2. 삽입 정렬 - 특정 데이터를 가장 적절한 위치에 삽입 // 거의 정렬되어 있을 때 효율적
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
  for j in range(i, 0, -1):
    if array[j] < array[j-1]:
      array[j], array[j-1] = array[j-1], array[j]
    else:
      break
      
print(array)

# 3. 퀵 정렬 - 기준 데이터를 설정하고 기준보다 큰 데이터와 작은 데이터를 스왑 // 거의 정렬시 비효율적
array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
  if start >= end : return # 원소가 1개인 경우 종료

  pivot = start # pivot은 첫 원소
  left = start + 1
  right = end

  # left와 right가 교차 전까지 반복
  while left <= right:
    # pivot보다 큰 left 찾기
    while left<= end and array[left] <= array[pivot]:
      left += 1
    # pivot보다 작은 right 찾기
    while right > start and array[right] >= array[pivot]:
      right -= 1

    if left > right: # 교차시 작은 데이터와 피벗을 교체
      array[right], array[pivot] = array[pivot], array[right]
    else: # 교차하지 않았다면 left와 right를 교체
      array[left], array[right] = array[right], array[left]

  # right(pivot)을 기준으로 다시 quicksort 진행
  quick_sort(array, start, right-1)
  quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)

# 4. 계수 정렬 - 모든 범위를 담는 리스트를 선언 // 데이터의 차이가 백만을 넘지 않도록한다
array = [7,5,9,0,3,1,6,2,4,8]

count = [0] * (max(array) + 1)

for i in range(len(array)):
  count[array[i]] += 1

for i in range(len(count)):
  for j in range(count[i]):
    print(i, end=' ')
