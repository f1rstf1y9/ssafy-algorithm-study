dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    queue = [(x,y)]
    matrix[y][x] = 0

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if matrix[ny][nx] == 1:
                queue.append((nx,ny))
                matrix[ny][nx] = 0

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        matrix[y][x] = 1
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                BFS(j, i)
                cnt += 1
    print(cnt)