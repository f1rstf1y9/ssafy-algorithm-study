from collections import deque
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y,x,n):
    q = deque([(y, x)])
    cnt = 0
    number[y][x] = n
    while q:
        y,x = q.popleft()
        cnt += 1
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < N and 0 <= nx < M and not number[ny][nx]:
                # 여기서 q에 해당 좌표가 들어있는지 판단해주지 않았을때 중복으로 탐색하므로 중복 카운트 및 시간초과
                if m_map[ny][nx] == '0':
                    q.append((ny,nx))
                    number[ny][nx] = n
    cnt_lst.append(cnt)

N, M = map(int, input().split())
m_map = [list(input()) for _ in range(N)]
number = [[0]*M for _ in range(N)]
cnt_lst = [0]

n = 1
for i in range(N):
    for j in range(M):
        if m_map[i][j] == '0' and not number[i][j]:
            bfs(i,j,n)
            n += 1

for i in range(N):
    for j in range(M):
        if m_map[i][j] == '1':
            answer = 0
            checked = []
            for k in range(4):
                y,x = i+dy[k], j+dx[k]
                if 0 <= y < N and 0 <= x < M and number[y][x] not in checked:
                    checked.append(number[y][x])
                    answer += cnt_lst[number[y][x]]
            print((answer+1)%10,end='')
        else:
            print(0,end='')
    print()
# print("==")
# print(cnt_lst)
# for a in number:
#     print(*a,sep='')