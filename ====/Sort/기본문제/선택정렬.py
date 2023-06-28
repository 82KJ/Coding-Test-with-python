# 가장 작은 원소를 찾아 앞으로 보내는 정렬
a = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(a)):
    min_index = i
    for j in range(i+1, len(a)):
        # i 이후의 배열에서 최소값 인덱스를 찾는다
        if a[min_index] > a[j]:
            min_index = j
    # i와 min_index의 위치를 swap한다
    a[i], a[min_index] = a[min_index], a[i] 

print(a)