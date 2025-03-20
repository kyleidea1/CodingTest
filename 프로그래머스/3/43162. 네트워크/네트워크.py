from collections import deque

def bfs(matrix,visited,cur):
    q = deque([cur])
    visited[cur] = True

    while q:
        v = q.popleft()
        for i in range(len(matrix)):
            if matrix[v][i] == 1 and not visited[i]:
                q.append(i)
                visited[i] = True
        
def solution(n,matrix):
    visited = [False]*n
    ans = 0
    
    for i in range(n):
        if not visited[i]:
            bfs(matrix,visited,i)
            ans += 1
            
    return ans



        
    
            

    
    
    






# def solution(n, computers):
#     answer = 0
#     visited = [False for _ in range(n)]
#     for i in range(n):
#         if visited[i] == False:
#             dfs(n, computers, i, visited)
#             answer += 1
#     return answer

# def dfs(n, computers, i, visited):
#     visited[i] = True
#     for j in range(n):
#         if visited[j] == False and i != j and computers[i][j] == 1:
#             dfs(n, computers, j, visited)