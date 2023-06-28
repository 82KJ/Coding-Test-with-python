from itertools import combinations

n = int(input())
map_data = []
blanks = []
teachers = []

for i in range(n):
    temp = list(input().split())
    map_data.append(temp)
    
    for j in range(n):
        if temp[j] == 'X':
            blanks.append((i,j))
        elif temp[j] == 'T':
            teachers.append((i,j))

cases = combinations(blanks,3)

dy = [-1,1,0,0]
dx = [0,0,-1,1]
flag = False

def check(y,x,direction):
    # 해당 방향에 대해서 한칸 진행
    yy = y + dy[direction]
    xx = x + dx[direction]

    # 만약 범위를 벗어나면, 발각 X => return False
    if yy < 0 or xx < 0 or yy >= n or xx >= n: return False

    # 만약 S를 발견하면, return True
    if map_data[yy][xx] == 'S': return True

    # 만약 O를 발견하면, 발각 X => return False
    if map_data[yy][xx] == 'O': return False

    # 뭣도 해당하지 않는다면, 다음칸 이동
    return check(yy,xx,direction)


for case in cases:
    for y,x in case:
        map_data[y][x] = 'O'
    
    # 모든 선생님 좌표에 대해서
    cnt1 = 0
    for y,x in teachers:
        is_ok = True
        # 모든 방향에 대해서,
        for i in range(4):
            # 발각이 되었다면,
            if check(y,x,i) == True:
                is_ok = False
                break
        # 모든 방향에서 하나도 발각이 안되면, 선생님 추가
        if is_ok == True:
            cnt1 += 1
        else: # 한명이라도 발각되면, 그냥 다음 case로 넘어감
            break
    
    if cnt1 == len(teachers):
        print("YES")
        flag = True
        break

    for y,x in case:
        map_data[y][x] = 'X'


if flag == False:
    print("NO")