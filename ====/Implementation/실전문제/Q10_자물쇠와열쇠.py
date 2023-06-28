def rotate(key):
    m = len(key)
    new_key = [[0]*m for _ in range(m)]
    
    for row in range(m):
        for col in range(m):
            new_key[col][m-row-1] = key[row][col]
    
    return new_key

def check(new_lock):
    lock_length = len(new_lock)//3

    for row in range(lock_length, lock_length*2):
        for col in range(lock_length, lock_length*2):
            if new_lock[row][col] != 1:
                return False
    return True


def solution(key, lock):
    m = len(key)
    n = len(lock)

    # 1. lock의 크기를 확장한다
    new_lock = [[0]*n*3 for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]
        
    # 2. 키를 회전시키면서 자물쇠와 맞춰본다
    for rotation in range(4):
        key = rotate(key)

        # new_lock에 대해서
        for row in range(n*2):
            for col in range(n*2):
                # key를 끼워 맞춘다
                for a in range(m):
                    for b in range(m):
                        new_lock[row+a][col+b] += key[a][b]

                # 자물쇠와 일치하는지 확인한다
                if check(new_lock): return True

                # key를 다시 풀어준다
                for a in range(m):
                    for b in range(m):
                        new_lock[row+a][col+b] -= key[a][b]
    
    return False
        

    
    