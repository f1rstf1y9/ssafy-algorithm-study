def get_parent(e):
    if parent[e] != e:
        parent[e] = get_parent(parent[e])
    return parent[e]

def union(e1, e2):
    a, b = get_parent(e1), get_parent(e2)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
M = int(input())
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x:x[2])
parent = [i for i in range(N+1)]
ans = 0
for edge in edges:
    e1, e2 = edge[0], edge[1]
    if get_parent(e1) != get_parent(e2):
        union(e1, e2)
        ans += edge[2]
print(ans)