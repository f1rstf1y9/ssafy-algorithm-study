from itertools import combinations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    queue = [(x,y)]
    copy_lab[x][y] = 2
    while queue:
        x, y = queue.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if copy_lab[nx][ny] == 0:
                copy_lab[nx][ny] = 2
                queue.append((nx,ny))

N, M = map(int, input().split())
lab = []
wall = []
max_safe = 0

for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(M):
        if lst[j] == 0:
            wall.append((i, j))
    lab.append(lst)

wall_comb = list(combinations(wall, 3))
for walls in wall_comb:
    copy_lab = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            copy_lab[i][j] = lab[i][j]
    for w in walls:
        copy_lab[w[0]][w[1]] = 1
    for i in range(N):
        for j in range(M):
            if copy_lab[i][j] == 2:
                BFS(i, j)
    safe = 0
    for i in range(N):
        for j in range(M):
            if copy_lab[i][j] == 0:
                safe += 1
    if safe > max_safe:
        max_safe = safe

print(max_safe)