# 1. 인풋 처리
n = input()
length = len(n)

# 2. 왼쪽 오른쪽 합 구하기
left = sum(list(map(int,n[:length//2])))
right = sum(list(map(int, n[length//2:])))

# 3. 결과 출력
if left == right: print("LUCKY")
else : print("READY")