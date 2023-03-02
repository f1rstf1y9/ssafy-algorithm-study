directions = [(),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]

def move_clouds(d, s):
    new_clouds = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if clouds[i][j]:
                y, x = (i+directions[d][0]*s)%N, (j+directions[d][1]*s)%N
                new_clouds[y][x] = 1
                grid[y][x] += 1
    return new_clouds

def water_copy():
    for i in range(N):
        for j in range(N):
            if clouds[i][j]:
                cnt = 0
                for k in range(2, 9, 2):
                    y, x = i+directions[k][0], j+directions[k][1]
                    if 0 <= y < N and 0 <= x < N and grid[y][x]:
                        cnt += 1
                grid[i][j] += cnt

def make_clouds():
    new_clouds = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if grid[i][j] >= 2 and not clouds[i][j]:
                new_clouds[i][j] = 1
                grid[i][j] -= 2
    return new_clouds

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
clouds = [[0]*N for _ in range(N)]
clouds[N-1][0] = clouds[N-1][1] = clouds[N-2][0] = clouds[N-2][1] = 1
for _ in range(M):
    d, s = map(int, input().split())
    clouds = move_clouds(d, s)
    water_copy()
    clouds = make_clouds()
ans = 0
for i in range(N):
    for j in range(N):
        ans += grid[i][j]
print(ans)