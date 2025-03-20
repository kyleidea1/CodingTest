from collections import deque

def solution(maps):
    rows, cols = len(maps), len(maps[0])
    visited = [[False]*cols for _ in range(rows)]
    
    q = deque([(0,0,1)])
    visited[0][0] = True
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while q:
        y,x,cnt = q.popleft()
        for i in range(4):
            ny,nx,ncnt = y + dy[i], x + dx[i], cnt + 1
            if 0<=ny<rows and 0<=nx<cols:
                if not visited[ny][nx] and maps[ny][nx] == 1:
                    if ny == rows - 1 and nx == cols - 1:
                        return ncnt
                    else:
                        visited[ny][nx] = True
                        q.append((ny,nx,ncnt))
                    
    return -1