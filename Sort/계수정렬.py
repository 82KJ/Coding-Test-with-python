# 계수 정렬은 최소값과 최대값의 차이가 적고, 정수 표현 범위일때, 사용 가능한 정렬

a = [7,5,9,0,3,1,6,2,4,8]

# counts는 배열의 최대값의 크기만큼 설정한다
count = [0]*(max(a)+1)

for i in a:
    count[i] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
