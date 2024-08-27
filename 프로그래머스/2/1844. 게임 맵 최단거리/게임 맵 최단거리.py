from collections import deque

def solution(maps):
    rows = len(maps)
    cols = len(maps[0])
    
    q = deque([])
    q.append((0,0,1))
    visited = [[False]*cols for _ in range(rows)]
    visited[0][0] = True
    
    while q:
        dm = (-1,1,0,0)
        dn = (0,0,-1,1)
        m,n,cnt = q.popleft()
        for i in range(4):
            nm, nn, ncnt = m+dm[i], n+dn[i], cnt+1
            if 0<=nm<rows and 0<=nn<cols and not visited[nm][nn] and maps[nm][nn] == 1:
                if nm == rows-1 and nn == cols-1:
                    return ncnt
                else:
                    visited[nm][nn] = True
                    q.append((nm,nn,ncnt))
    return -1
            