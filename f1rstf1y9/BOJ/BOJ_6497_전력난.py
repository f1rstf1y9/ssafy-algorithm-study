import sys
input = sys.stdin.readline

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

while True:
    m, n = map(int, input().rstrip().split())
    if (m, n) == (0, 0):
        break
    edges = [list(map(int, input().rstrip().split())) for _ in range(n)]
    edges.sort(key=lambda x:x[2])
    parent = [i for i in range(m+1)]

    cost = 0
    for edge in edges:
        cost += edge[2]
        if get_parent(edge[0]) != get_parent(edge[1]):
            union(edge[0], edge[1])
            cost -= edge[2]
    print(cost)