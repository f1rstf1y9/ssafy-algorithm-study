import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def get_parent(n):
    if parents[n] == n:
        return n
    parents[n] = get_parent(parents[n])
    return parents[n]

def union(e1, e2):
    a, b = get_parent(e1), get_parent(e2)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def dfs(start, cur, cost):
    for n, c in road[cur]:
        if not visited[n]:
            visited[n] = 1
            dist[start][n] = max(cost, c)
            dfs(start, n, dist[start][n])

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x:x[2])
Q = int(input())
parents = [i for i in range(N + 1)]
road = [[] for _ in range(N+1)]
dist = [[0]*(N+1) for _ in range(N+1)]
mst = 0
for edge in edges:
    e1, e2, c = edge
    if get_parent(e1) != get_parent(e2):
        road[e1].append((e2, c))
        road[e2].append((e1, c))
        union(e1, e2)
        mst += c
for i in range(1,N+1):
    visited = [0]*(N+1)
    visited[i] = 1
    dfs(i, i, 0)

for _ in range(Q):
    X, Y = map(int, input().split())
    print(mst-dist[X][Y])