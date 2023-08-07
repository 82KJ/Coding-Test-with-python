# 1. 인풋 처리
n = int(input())

arr = list()
for i in range(n):
  a,b,c,d = input().split()
  arr.append((a, int(b), int(c), int(d)))

# 2. 국어 내림차순, 영어 오름차순, 수학 내림차순, 이름 오름차순
arr.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))

for x in arr:
  print(x[0])


          