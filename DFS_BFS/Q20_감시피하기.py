from itertools import combinations

# 1. 인풋 처리
n = int(input())
graph = list()
teachers = list()
blanks = list()

for i in range(n):
  temp = list(input().split())
  graph.append(temp)

  for j in range(n):
    if temp[j] == 'T':
      teachers.append((i,j))
    elif temp[j] == 'X':
      blanks.append((i,j))

# dfs로 같은 방향에 S가 있는지 탐색
def dfs(cur, graph, direc):
  cur_y, cur_x = cur

  # 종료 조건 -> 벽에 부딫힘
  if cur_y < 0 or cur_x < 0 or cur_y >= n or cur_x >= n:
    return True

  # 종료 조건 -> 장애물에 부딫힘
  if graph[cur_y][cur_x] == 'O':
    return True

  # 종료 조건 -> 학생에 부딫힘
  if graph[cur_y][cur_x] == 'S':
    return False

  ny = cur_y + direc[0]
  nx = cur_x + direc[1]

  return dfs((ny,nx), graph, direc)
   
# 2. 장애물 경우의 수 순회
for case in list(combinations(blanks,3)):
  flag = True

  # 장애물 배치
  for obstacle in case:
    o_y, o_x = obstacle
    graph[o_y][o_x] = 'O'

  # 모든 선생님을 순회하면서, 걸리는 학생이 있는지 확인
  for teacher in teachers:
    for direc in [(-1,0), (1,0), (0,1), (0,-1)]:
      if dfs(teacher, graph, direc) == False:
        flag = False
        break
    if flag == False:
      break

  if flag == True:
    break

  # 장애물 치우기
  for obstacle in case:
    o_y, o_x = obstacle
    graph[o_y][o_x] = 'X'
    
if flag == True:
  print("YES")
else:
  print("NO")