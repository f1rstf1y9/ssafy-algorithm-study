import sys
input = sys.stdin.readline

di = [0, (-1,0), (1,0), (0,1), (0,-1)]
def change_coord(y, x, dir, s):
    move_y, move_x = abs(s[0]*dir[0]), abs(s[1]*dir[1])
    dy, dx = dir
    while move_y:
        if y+dy < 0:
            dy = 1
        elif y+dy >= R:
            dy = -1
        temp = min(move_y, y if dy < 0 else R - y - 1)
        y += temp*dy
        move_y -= temp
    while move_x:
        if x+dx < 0:
            dx = 1
        elif x+dx >= C:
            dx = -1
        temp = min(move_x, x if dx<0 else C-x-1)
        x += temp*dx
        move_x -= temp
    return (y, x, di.index((dy,dx)))

def move_shark():
    new_grid = [[0]*C for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if grid[y][x]:
                s, d, z = grid[y][x]
                ny, nx, d = change_coord(y, x, di[d], s)
                if not new_grid[ny][nx] or new_grid[ny][nx][2] < z:
                    new_grid[ny][nx] = (s, d, z)
    return new_grid

R, C, M = map(int, input().split())
grid = [[0]*C for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sy, sx = s%(R*2-2), s%(C*2-2)
    grid[r-1][c-1] = ((sy,sx),d,z) #(속력, 방향, 크기)

catch = 0
for x in range(C):
    for y in range(R):
        if grid[y][x]:
            catch += grid[y][x][2]
            grid[y][x] = 0
            break
    grid = move_shark()
print(catch)