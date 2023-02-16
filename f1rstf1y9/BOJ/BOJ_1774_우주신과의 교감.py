import sys
input = sys.stdin.readline

def get_dist(g1, g2):
    return ((g1[0]-g2[0])**2 + (g1[1]-g2[1])**2)**0.5

def get_parent(e):
    if parent[e] != e:
        parent[e] = get_parent(parent[e])
    return parent[e]

def union(e1, e2):
    a, b = get_parent(e1), get_parent(e2)
    if a < b:
        parent[b] = get_parent(a)
    else:
        parent[a] = get_parent(b)

N, M = map(int, input().split())
gods = [list(map(int, input().split())) for _ in range(N)]
parent = [i for i in range(N)]
exist_edges = []
edges = []
ans = 0
for _ in range(M):
    g1, g2 = map(int, input().split())
    union(g1-1, g2-1)
    exist_edges.extend([[g1-1, g2-1], [g2-1, g1-1]])
for i in range(N):
    for j in range(i+1, N):
        g1, g2 = gods[i], gods[j]
        edges.append([get_dist(g1, g2), i, j])
edges.sort()
for edge in edges:
    if get_parent(edge[1]) != get_parent(edge[2]):
        union(edge[1], edge[2])
        ans += edge[0]
print(f"{ans:.2f}")