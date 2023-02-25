percent = [[0,0,2,0,0],[0,10,7,1,0],[5,'a',0,0,0],[0,10,7,1,0],[0,0,2,0,0]]
d = [(0, -1), (1, 0), (0, 1), (-1, 0)]

# 5x5 퍼센트 이차원 리스트를 시계반대 방향으로 90도 회전
def rotate(lst):
    n = len(lst)
    m = len(lst[0])
    new = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[n-1-j][i] = lst[i][j]
    return new


# 퍼센트 리스트의 값에 따라 해당 위치에 모래 날려보내기
def move_sand(y,x):
    sand = remain = grid[y][x]
    grid[y][x] = 0
    out = mv_y = mv_x = 0

    # 퍼센트 리스트 조회하면서 모래 날리기
    for i in range(5):
        for j in range(5):
            ny, nx = y+i-2, x+j-2
            p = percent[i][j]
            if p == 'a':
                mv_y, mv_x = y+i-2, x+j-2
                continue
            if not p:
                continue
            s = int(sand * p / 100)
            remain -= s
            if 0 <= ny < N and 0 <= nx < N:
                grid[ny][nx] += s
            else:
                out += s

    # 퍼센트대로 날리고 남은 모래 옮기기
    if 0 <= mv_y < N and 0 <= mv_x < N:
        grid[mv_y][mv_x] += remain
    else:
        out += remain

    return out

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
y, x = N//2, N//2

# 소용돌이 형태로 한칸씩 조회하기
ans = cnt = 0
for k in range(1, N + 1):
    for _ in range(2):
        for i in range(k):
            if grid[y][x]:
                ans += move_sand(y, x)
            if (y, x) != (N//2, N//2) and i == 0:
                percent = rotate(percent)
            y, x = y+d[cnt%4][0], x+d[cnt%4][1]
        cnt += 1

        if not (0 <= y < N and 0 <= x < N):
            break
print(ans)