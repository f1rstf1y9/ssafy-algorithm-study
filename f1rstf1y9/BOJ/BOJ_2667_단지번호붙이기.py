dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x):
    visited[y][x] = 1
    danji[-1] += 1
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if apart[ny][nx] == 1 and not visited[ny][nx]:
                bfs(ny, nx)

N = int(input())
apart = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
danji = []
for i in range(N):
    for j in range(N):
        if apart[i][j] == 1 and not visited[i][j]:
            danji.append(0)
            bfs(i, j)
print(len(danji))
print(*sorted(danji), sep='\n')