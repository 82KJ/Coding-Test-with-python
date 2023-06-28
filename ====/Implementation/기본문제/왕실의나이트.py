n = input()
col = ord(n[0]) - ord('a') + 1 # 문자를 유니코드로 변환하는 ord 함수를 이용
row = int(n[1])

# 상,하,좌,우
dy = [-2,-2,2,2,-1,1,-1,1]
dx = [-1,1,-1,1,-2,-2,2,2]

cnt = 0
for i in range(8):
    yy = row + dy[i]
    xx = col + dx[i]

    if yy < 1 or yy > 8 or xx < 1 or xx > 8 : continue
    cnt +=1

print(cnt)