import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(cur):
    global cnt_g, cnt_d
    visited[cur] = 1
    lc = len(graph[cur])

    # ㅈ 세기
    if lc >= 3:
        cnt_g += lc*(lc-1)*(lc-2)//(3*2*1)

    # ㄷ 세기
    for i in range(lc):
        next = graph[cur][i]
        ln = len(graph[next])
        if ln >= 2 and not visited[next]:
            if lc >= 2:
                cnt_d += (lc-1)*(ln-1)
            dfs(next)

N = int(input().rstrip())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(N-1):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)
cnt_g = cnt_d = 0
dfs(1)
if cnt_d > cnt_g*3:
    print('D')
elif cnt_d < cnt_g*3:
    print('G')
else:
    print('DUDUDUNGA')
