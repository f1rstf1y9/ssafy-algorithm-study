dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def cnt_seat(y,x,l):
    cnt_l = cnt_z = 0
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if grid[ny][nx] in l:
                cnt_l += 1
            if not grid[ny][nx]:
                cnt_z += 1
    return cnt_l, cnt_z

N = int(input())
grid = [[0]*N for _ in range(N)]
likes = [[] for _ in range(N**2+1)]
for _ in range(1,N**2+1):
    max_likes = -1
    cur_zeros = 0
    seat = []
    s = list(map(int, input().split()))
    likes[s[0]].extend(s[1:])
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            if not grid[i][j]:
                like, zero = cnt_seat(i, j, s[1:])
                if like > max_likes:
                    max_likes, cur_zeros = like, zero
                    seat = [i, j]
                elif like == max_likes:
                    if zero >= cur_zeros:
                        seat = [i, j]
                        cur_zeros = zero
    grid[seat[0]][seat[1]] = s[0]

ans = 0
for i in range(N):
    for j in range(N):
        ans += int(10**(cnt_seat(i, j, likes[grid[i][j]])[0]-1))
print(ans)