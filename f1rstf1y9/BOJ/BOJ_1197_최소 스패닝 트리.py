def get_parent(n):
    if cycle[n] == n:
        return n
    cycle[n] = get_parent(cycle[n])
    return cycle[n]

def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)
    if a < b:
        cycle[b] = a
    else:
        cycle[a] = b
V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
cycle = [0]+[i for i in range(1,V+1)]
finished = [0]+[1]*V
edges.sort(key=lambda x:x[2], reverse=True)
ans = 0
while edges and cycle != finished:
    edge = edges.pop()
    if get_parent(edge[0]) == get_parent(edge[1]):
        continue
    union_parent(edge[0], edge[1])
    ans += edge[2]
print(ans)