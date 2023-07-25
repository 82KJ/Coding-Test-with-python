from collections import deque

def get_next_pos(pos, board):
    next_pos = []
    
    pos = list(pos) # 현재 위치
    y1, x1, y2, x2 = pos[0][0],pos[0][1],pos[1][0],pos[1][1]
    
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    
    # 1. 상, 하, 좌, 우 이동 처리
    for d in [(1,0),(-1,0),(0,1),(0,-1)]:
        yy1, xx1, yy2, xx2 = y1 + d[0], x1 + d[1], y2 + d[0], x2 + d[1]
        
        # 만약, 해당 두 칸이 모두 비어있다면, 이동한다
        if board[yy1][xx1] == 0 and board[yy2][xx2] == 0:
            next_pos.append({(yy1,xx1), (yy2,xx2)})
    
    # 2. 회전 처리
    # 현재 로봇이 가로인 경우
    if y1 == y2:
        for i in [-1,1]: # 위, 아래 회전
            # 위 또는 아래의 블록 두개가 비어있어야만, 회전한다
            if board[y1 + i][x1] == 0 and board[y2 + i][x2] == 0:
                next_pos.append({(y1,x1),(y1+i,x1)})
                next_pos.append({(y2,x2), (y2+i,x2)})
    # 현재 로봇이 세로인 경우
    else:
        for i in [-1,1]: # 왼쪽, 오른쪽 회전
            # 왼쪽 또는 오른쪽의 블록 두개가 비어있어야만, 회전한다
            if board[y1][x1+i] == 0 and board[y2][x2+i] == 0:
                next_pos.append({(y1,x1),(y1,x1+i)})
                next_pos.append({(y2,x2), (y2,x2+i)})
    
    return next_pos
    
    
def solution(board):
    answer = 0
    
    n = len(board)
     
    # 1. 맵의 외곽을 형성한다 => robot이 맵을 벗어나는지 편하게 관찰
    new_board = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]

    # 2. BFS를 수행하며, 최단 경로를 찾는다
    robot = deque()
    visited = []

    pos = {(1,1), (1,2)} # 집합 자료형으로 관리한다
    robot.append((pos,0))
    visited.append(pos)
    
    while robot:
        pos, cost = robot.popleft()
        
        # 만약, 도착 지점에 도달하면 cost를 반환한다
        if (n,n) in pos: return cost
        
        # 3. 현재 위치로부터 다음에 이동가능한 모든 pos에 대하여,
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                robot.append((next_pos, cost+1))
                visited.append(next_pos)
    
    return answer