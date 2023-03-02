'''
한칸씩 돌면서 아직 연합에 없는 나라에 한해 국경선을 열수 있는지 없는 지 확인
국경선 열 수 있으면 연합 리스트에 추가
연합 리스트에 존재하는 나라들 인구수 변경
위 과정 반복
'''

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y,x):
    unites = [] # 국경선 오픈한 나라들
    unites_pop = 0
    q = [(y,x)]
    while q:
        y, x = q.pop()
        if (y,x) not in unites:
            unites.append((y,x))
            unites_pop += countries[y][x]
        visited[y][x] = 1
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                if L <= abs(countries[y][x] - countries[ny][nx]) <= R:
                    q.append((ny,nx))
    if len(unites) == 1:
        return False
    pop = unites_pop // len(unites)
    while unites:
        y, x = unites.pop()
        countries[y][x] = pop
    return True
N, L, R = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(N)]
isOpen = True
day = -1
while isOpen:
    day += 1
    # 오늘 이 국가를 방문했는지 판단할 리스트
    visited = [[0] * N for _ in range(N)]
    isOpen = False
    for i in range(N):
        for j in range(N):
            # 아직 이 나라 방문X
            if not visited[i][j]:
                if bfs(i,j): # 탐색해서 국경 오픈했는지 확인
                    isOpen = True
print(day)