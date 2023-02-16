import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

N, M, K = map(int, input().rstrip().split())
alpha_map = [list(input().rstrip()) for _ in range(N)]
alpha_list = {}
god_like_str = []
for _ in range(K):
    s = input().rstrip()
    god_like_str.append(s)
    alpha_list[s] = 0

def dfs(x, y, string):
    if string in alpha_list:
        alpha_list[string] += 1
    if len(string) == 5:
        return
    for i in range(8):
        nx, ny = (x+dx[i])%N, (y+dy[i])%M
        dfs(nx, ny, string+alpha_map[nx][ny])

for i in range(N):
    for j in range(M):
        string = ''
        dfs(i,j,string + alpha_map[i][j])

for s in god_like_str:
    print(alpha_list[s])