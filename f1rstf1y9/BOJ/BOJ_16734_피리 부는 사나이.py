import sys
sys.setrecursionlimit(10**6)

cnt = 0
def dfs(x, y):
    global cnt
    visited[x][y] = 1
    history.append((x, y))
    d = direction[p_map[x][y]]
    nx, ny = x+d[0], y+d[1]
    if visited[nx][ny] == 1:
        if (nx,ny) in history:
            cnt += 1
        return
    else:
        dfs(nx, ny)

N, M = map(int, input().split())
direction = {'D':(1,0), 'U':(-1,0), 'L':(0,-1), 'R':(0,1)}
p_map = [input() for _ in range(N)]
visited = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            history = []
            dfs(i,j)
print(cnt)