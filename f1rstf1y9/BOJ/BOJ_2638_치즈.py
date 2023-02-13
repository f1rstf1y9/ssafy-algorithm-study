import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def is_cheese():
    for i in range(N):
        for j in range(M):
            if grid[i][j]:
                return True
    return False

day = 0
while is_cheese():
    temp = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            temp[i][j] = grid[i][j]

    stack = [(0, 0)]
    visited = [[False] * M for _ in range(N)]
    while stack:
        x, y = stack.pop()
        visited[x][y] = True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:
                    if grid[nx][ny]:
                        grid[nx][ny] += 1
                    else:
                        visited[nx][ny] = True
                        stack.append((nx, ny))
    for i in range(N):
        for j in range(M):
            if grid[i][j] > 2:
                temp[i][j] = 0
            elif grid[i][j]:
                temp[i][j] = 1
            grid[i][j] = temp[i][j]
    day += 1
print(day)