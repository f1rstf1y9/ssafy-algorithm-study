import sys
sys.setrecursionlimit(10**9)

def dfs(n, w):
    cheer[n] += w
    if not graph[n]:
        return
    for i in range(len(graph[n])):
        dfs(graph[n][i], cheer[n])

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
parent = [-1] + list(map(int, input().split()))
cheer = [0]*(n+1)
for i in range(2, n+1):
    p = parent[i]
    graph[p].append(i)
for _ in range(m):
    i, w = map(int, input().split())
    cheer[i] += w
dfs(1, 0)
print(*cheer[1:])