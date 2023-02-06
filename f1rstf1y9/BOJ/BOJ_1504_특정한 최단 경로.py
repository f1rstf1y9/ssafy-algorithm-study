from heapq import heappush, heappop
import sys

input = sys.stdin.readline
INF = int(1e9)
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1, v2 = map(int, input().split())

def dijkstra(s):
    dist = [INF] * (N + 1)
    heap = []
    heappush(heap,(0, N))
    dist[s] = 0
    for node in graph[s]:
        if dist[node[0]] > node[1]:
            dist[node[0]] = node[1]
            heappush(heap,(node[1], node[0]))

    while heap:
        now = heappop(heap)[1]
        for node in graph[now]:
            cost = dist[now] + node[1]
            if dist[node[0]] > cost:
                dist[node[0]] = cost
                heappush(heap, (cost, node[0]))

    return dist

dist = dijkstra(1)
from_v1 = dijkstra(v1)
from_v2 = dijkstra(v2)

a = dist[v1] + from_v1[v2] + from_v2[N]
b = dist[v2] + from_v2[v1] + from_v1[N]
if min(a, b) < INF:
    print(min(a, b))
else:
    print(-1)
