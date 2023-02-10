N = int(input())
grid = [list(input()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y, c):
    stack = [(x,y)]   
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if grid[nx][ny] == c and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    if c == 'G':
                        grid[nx][ny] = 'R'
                    stack.append((nx,ny))

no_cnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = 1
            BFS(i, j, grid[i][j])
            if grid[i][j] == 'G':
                grid[i][j] = 'R'
            no_cnt += 1

yes_cnt = 0
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = 1
            BFS(i, j, grid[i][j])
            yes_cnt += 1

print(no_cnt, yes_cnt)