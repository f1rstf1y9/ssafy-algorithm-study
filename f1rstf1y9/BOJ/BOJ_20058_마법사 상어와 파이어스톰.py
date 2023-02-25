dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def rotate(y, x, n):
    lst = []
    for i in range(n):
        temp = []
        for j in range(n-1, -1, -1):
            temp.append(ice[y+j][x+i])
        lst.append(temp)
    for i in range(n):
        for j in range(n):
            ice[y+i][x+j] = lst[i][j]

def magic(n):
    for i in range(0, N, 2**n):
        for j in range(0, N, 2**n):
            rotate(i,j,2**n)

def is_melt(y, x):
    cnt = 0
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if ice[ny][nx]:
                cnt += 1
    if cnt < 3:
        check[y][x] = 1

def bfs(y, x):
    d = 0
    q = [(y, x)]
    while q:
        y, x = q.pop()
        if not visited[y][x]:
            d += 1
        visited[y][x] = 1
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if ice[ny][nx] and not visited[ny][nx]:
                    q.append((ny, nx))
    return d

N, Q = map(int, input().split())
N = 2**N
ice = [list(map(int, input().split())) for _ in range(N)]
magic_order = list(map(int,input().split()))
for n in magic_order:
    check = [[0]*N for _ in range(N)]
    magic(n)
    for i in range(N):
        for j in range(N):
            is_melt(i, j)
    for i in range(N):
        for j in range(N):
            if check[i][j] and ice[i][j]:
                ice[i][j] -= 1

visited = [[0]*N for _ in range(N)]
cnt = max_d = 0
for i in range(N):
    for j in range(N):
        cnt += ice[i][j]
        if ice[i][j] and not visited[i][j]:
            d = bfs(i, j)
            if max_d < d:
                max_d = d

print(cnt)
print(max_d)