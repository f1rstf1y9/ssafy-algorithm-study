import sys
sys.setrecursionlimit(10**9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(y, x):
    visited[y][x] = 1
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < Y and 0 <= nx < X:
            if cheese[ny][nx] == 1:
                cheese[ny][nx] = 2
            if cheese[ny][nx] == 0 and not visited[ny][nx]:
                bfs(ny, nx)

def cnt_cheese():
    cnt = 0
    for i in range(Y):
        for j in range(X):
            if cheese[i][j] == 1:
                cnt += 1
            if cheese[i][j] == 2:
                cheese[i][j] = 0
    return cnt

Y, X = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(Y)]
cheese_cnt = temp = cnt_cheese()
day = 0
while cheese_cnt != 0:
    temp = cheese_cnt
    visited = [[0]*X for _ in range(Y)]
    bfs(0, 0)
    day += 1
    cheese_cnt = cnt_cheese()
print(day)
print(temp)
