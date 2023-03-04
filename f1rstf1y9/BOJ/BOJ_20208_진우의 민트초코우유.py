def dfs(y,x,hp,m): # 좌표, 체력, 민초
    global max_mincho

    for i in range(len(mincho)):
        if not visited[i]:
            k = abs(y-mincho[i][0])+abs(x-mincho[i][1])
            if hp >= k:
                visited[i] = 1
                dfs(mincho[i], hp+H-k, m+1)
                visited[i] = 0

    if abs(hy-y)+abs(hx-x) <= hp:
        max_mincho = max(m, max_mincho)

N, M, H = map(int, input().split())
m_map = [list(map(int, input().split())) for _ in range(N)]
mincho = []
hy = hx = 0

max_mincho = 0
for i in range(N):
    for j in range(N):
        if m_map[i][j] == 1:
            hy, hx = i, j
        if m_map[i][j] == 2:
            mincho.append([i,j])
visited = [0]*len(mincho)
dfs(hy, hx, M, 0)
print(max_mincho)