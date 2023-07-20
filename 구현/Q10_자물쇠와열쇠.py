def rotate_key(key):
    m = len(key)
    new_key = [[0]*m for _ in range(m)]
    
    for i in range(m):
        for j in range(m):
            new_key[i][j] = key[m-1-j][i]
    
    return new_key

def is_lock_pick(new_lock, n):
    for i in range(n, 2*n):
        for j in range(n, 2*n):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    answer = False
    
    # 1. lock 확장
    n = len(lock)
    m = len(key)
    new_lock = [[0]*(3*n) for _ in range(3*n)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    # 2. 4방향 순회
    for i in range(4):
        key = rotate_key(key)
        
        # 3. 한칸씩 이동하면서 일치 여부 확인
        for y in range(2*n):
            for x in range(2*n):
                
                for j in range(m):
                    for k in range(m):
                        new_lock[y+j][x+k] += key[j][k]
                        
                if is_lock_pick(new_lock, n) == True:
                    return True
                
                for j in range(m):
                    for k in range(m):
                        new_lock[y+j][x+k] -= key[j][k]
                
    return answer