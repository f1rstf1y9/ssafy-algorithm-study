dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_len, cnt = 0, 1
def dfs(x,y):
    global max_len, cnt
    if cnt > max_len:
            max_len = cnt
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            o = ord(grid[nx][ny])-65
            if not visited[o]:
                visited[o] = 1
                cnt += 1
                dfs(nx, ny)
                cnt -= 1
                visited[o] = 0
R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]
lst = [grid[0][0]]
visited = [0 for i in range(26)]
visited[ord(grid[0][0])-65] = 1
dfs(0,0)
print(max_len)