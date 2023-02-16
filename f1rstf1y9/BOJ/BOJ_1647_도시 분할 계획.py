import sys
input = sys.stdin.readline

def get_parent(edge):
    if parent[edge] != edge:
        parent[edge] = get_parent(parent[edge])
    return parent[edge]

def union(e1, e2):
    a = get_parent(e1)
    b = get_parent(e2)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x:x[2])
parent = [i for i in range(N+1)]

cost = []
for edge in edges:
    if get_parent(edge[0]) != get_parent(edge[1]):
        union(edge[0], edge[1])
        cost.append(edge[2])
print(sum(cost) - max(cost))