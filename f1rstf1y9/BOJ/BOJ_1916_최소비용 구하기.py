from heapq import heappop, heappush
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
INF = int(1e9)
dist = [INF]*(N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((e,w))

S, E = map(int, input().split())

q = []
heappush(q, (0,S))
dist[S] = 0

while q:
    cur, x = heappop(q)
    if dist[x] < cur:
        continue
    for node in graph[x]:
        cost = dist[x] + node[1]
        if dist[node[0]] > cost:
            dist[node[0]] = cost
            heappush(q, (cost,node[0]))
            
print(dist[E])