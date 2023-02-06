from heapq import heappush, heappop
import sys
input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
INF = int(1e9)
dist = [INF]*(V+1)
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    heap = []
    heappush(heap, (0, start))
    dist[start] = 0

    while heap:
        now = heappop(heap)[1]
        for node in graph[now]:
            cost = dist[now] + node[1]
            if dist[node[0]] > cost:
                dist[node[0]] = cost
                heappush(heap, (cost, node[0]))

dijkstra(K)

for i in range(1, V+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])