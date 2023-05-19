from collections import deque

N, M = map(int, input().split())
coin_map = [list(input()) for _ in range(N)]
coins = []
for i in range(N):
    for j in range(M):
        if coin_map[i][j] == 'o':
            coins.append((i,j))
q = deque([(coins[0][0],coins[0][1],coins[1][0],coins[1][1],0)])
delta = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs():
    while q:
        x1,y1,x2,y2,cnt = q.popleft()
        for dx,dy in delta:
            nx1, ny1, nx2, ny2 = x1+dx, y1+dy, x2+dx, y2+dy
            if (0 <= nx1 < N and 0 <= ny1 < M) and not (0 <= nx2 < N and 0 <= ny2 < M):
                return cnt+1
            if not (0 <= nx1 < N and 0 <= ny1 < M) and (0 <= nx2 < N and 0 <= ny2 < M):
                return cnt+1
            if cnt+1 > 10:
                return -1
            if (0 <= nx1 < N and 0 <= ny1 < M) and (0 <= nx2 < N and 0 <= ny2 < M):
                if coin_map[nx1][ny1] == '#':
                    nx1, ny1 = x1, y1
                if coin_map[nx2][ny2] == '#':
                    nx2, ny2 = x2, y2
                q.append((nx1, ny1, nx2, ny2, cnt+1))
    return -1

print(bfs())
