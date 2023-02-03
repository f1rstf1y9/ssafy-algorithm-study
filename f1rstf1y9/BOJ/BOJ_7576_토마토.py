dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

M, N = map(int, input().split())
tomato = []
tomato_total = 0
not_tomato = 0
for i in range(N):
    tomato.append(list(map(int, input().split())))
    tomato_total += sum(tomato[i])
    not_tomato += tomato[i].count(-1)
    
stack = []
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            stack.append((i,j))

day = 0
new_stack = []
while stack:
    x, y = stack.pop()
    tomato[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if tomato[nx][ny] == 0:
            tomato[nx][ny] = 1
            new_stack.append((nx, ny))
    if not stack:
        stack = new_stack
        new_stack = []
        day += 1

for i in range(N):
    if 0 in tomato[i]:
        print(-1)
        break
else:
    print(day-1)