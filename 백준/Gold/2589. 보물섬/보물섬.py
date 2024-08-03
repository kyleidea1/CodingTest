import sys
from collections import deque

def bfs(x, y, matrix):
    INF = 987654321
    q = deque([(x, y)])
    distance = [[INF] * len(matrix[0]) for _ in range(len(matrix))]
    distance[x][y] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x,y = q.popleft()
        new_dist = distance[x][y] + 1
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= len(matrix) or ny < 0 or ny >= len(matrix[0]):
                continue
            if matrix[nx][ny] == 'L' and new_dist < distance[nx][ny]:
                distance[nx][ny] = new_dist
                q.append((nx, ny))
    valid_distance = [num for row in distance for num in row if num != INF]
    return max(valid_distance)

def main():
    input = sys.stdin.readline
    a, b = map(int, input().split())
    matrix = [input().strip() for _ in range(a)]
    cnt_list = []

    for i in range(a):
        for j in range(b):
            if matrix[i][j] == 'L':
                cnt_list.append(bfs(i,j,matrix))
    
    print(max(cnt_list))

if __name__ == "__main__":
    main()