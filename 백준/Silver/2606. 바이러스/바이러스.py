import sys
from collections import deque

a = int(input())
b = int(input())
graph = [[] for _ in range(a+1)]
for _ in range(b):
    c,d = map(int, input().split())
    graph[c].append(d)
    graph[d].append(c)
    # 양방향 그래프

q = deque([1]) 
visited = [False]*(a+1)
visited[1] = True
# 큐, 방문, 그래프 시작점 초기화
cnt = 0

while q:
    v = q.popleft()
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            q.append(i)
            cnt += 1

print(cnt)