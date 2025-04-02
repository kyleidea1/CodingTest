from collections import deque
            
def bfs(n,tree):
    cnt = 1
    q = deque([1])
    visited = [False]*(n+1)
    visited[1] = True
    
    while q:
        cur = q.popleft()
        for nex in tree[cur]:
            if not visited[nex]:
                visited[nex] = True
                q.append(nex)
                cnt += 1
                
    return cnt
    
def solution(n, wires):
    cnt_list = []
    for i in range(n-1):
        tmp = wires[i]
        wires[i] = [0,0] # wire 하나씩 끊으면서
        tree = [[] for _ in range(n+1)] # tree 다시 생성
        for start,target in wires:
            tree[start].append(target)
            tree[target].append(start)
        cnt_list.append(bfs(n,tree))
        wires[i] = tmp # wire 다시 메꾸기
    ans = min([abs(n-2*cnt_list[i]) for i in range(len(cnt_list))])
    return ans