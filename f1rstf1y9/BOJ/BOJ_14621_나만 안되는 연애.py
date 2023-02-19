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

N, M = map(int, input().split())
gender = [''] + input().split()
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x:x[2])
parent = [i for i in range(N+1)]
ans = 0
for edge in edges:
    if gender[edge[0]] == gender[edge[1]]:
        continue
    if get_parent(edge[0]) != get_parent(edge[1]):
        union(edge[0], edge[1])
        ans += edge[2]
for i in range(1, N+1):
    if parent[i] != 1:
        parent[i] = get_parent(i)
if sum(parent[1:]) != N:
    print(-1)
else:
    print(ans)