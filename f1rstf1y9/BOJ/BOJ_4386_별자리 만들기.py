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

def get_dist(s1, s2):
    return ((s1[0]-s2[0])**2 + (s1[1]-s2[1])**2)**0.5
n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]
parent = [i for i in range(n)]
edges = []
for i in range(n):
    for j in range(i+1, n):
        edges.append((get_dist(stars[i], stars[j]), i, j))
edges.sort()
ans = 0
for edge in edges:
    if get_parent(edge[1]) != get_parent(edge[2]):
        ans += edge[0]
        union(edge[1], edge[2])
print(f"{ans:.2f}")
