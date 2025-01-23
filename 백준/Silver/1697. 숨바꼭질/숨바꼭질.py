import sys
from collections import deque
input = sys.stdin.readline

a,b = map(int,input().split())
graph = [False] * 100001
ans = 0

q = deque([(a,0)])
graph[a] = True
while q:
    pos,sec = q.popleft()
    if 0<=pos-1<100001 and not graph[pos-1]:
        if pos-1 == b:
            ans = sec+1
            break
        q.append((pos-1,sec+1))
        graph[pos-1] = True
    if 0<=pos+1<100001 and not graph[pos+1]:
        if pos+1 == b:
            ans = sec+1
            break
        q.append((pos+1,sec+1))
        graph[pos+1] = True
    if 0<=2*pos<100001 and not graph[2*pos]:
        if 2*pos == b:
            ans = sec+1
            break
        q.append((2*pos,sec+1))
        graph[2*pos] = True
print(ans)