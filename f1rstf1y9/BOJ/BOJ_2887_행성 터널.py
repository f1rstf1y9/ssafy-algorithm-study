import sys
input = sys.stdin.readline

def get_parent(edge):
    if parent[edge] != edge:
        parent[edge] = get_parent(parent[edge])
    return parent[edge]

def union(e1, e2):
    a, b = get_parent(e1), get_parent(e2)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
planets = [[i] + list(map(int, input().split())) for i in range(N)]
parent = [i for i in range(N)]
edges = []
x_close_planets = sorted(planets, key=lambda x:x[1])
y_close_planets = sorted(planets, key=lambda x:x[2])
z_close_planets = sorted(planets, key=lambda x:x[3])
for i in range(N-1):
    p1, p2 = x_close_planets[i], x_close_planets[i+1]
    edges.append([min(abs(p1[1]-p2[1]),abs(p1[2]-p2[2]),abs(p1[3]-p2[3])), p1[0], p2[0]])

    p3, p4 = y_close_planets[i], y_close_planets[i+1]
    edges.append([min(abs(p3[1]-p4[1]),abs(p3[2]-p4[2]),abs(p3[3]-p4[3])), p3[0], p4[0]])

    p5, p6 = z_close_planets[i], z_close_planets[i+1]
    edges.append([min(abs(p5[1]-p6[1]),abs(p5[2]-p6[2]),abs(p5[3]-p6[3])), p5[0], p6[0]])

edges.sort()
ans = 0
for edge in edges:
    if get_parent(edge[1]) != get_parent(edge[2]):
        union(edge[1], edge[2])
        ans += edge[0]
print(ans)