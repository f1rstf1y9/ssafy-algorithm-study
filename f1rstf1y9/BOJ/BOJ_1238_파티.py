from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())
INF = int(1e9)
graph = [[]*(N+1) for _ in range(N+1)]
for _ in range(M):
    s,e,t = map(int, input().split())
    graph[s].append((e, t))

def dijkstra(S):
    dist = [INF]*(N+1)
    q = []
    heappush(q, (0, S))
    dist[S] = 0

    while q:
        n = heappop(q)
        if dist[n[1]] < n[0]:
            continue
        for node in graph[n[1]]:
            cost = dist[n[1]] + node[1]
            if dist[node[0]] > cost:
                dist[node[0]] = cost
                heappush(q, (cost, node[0]))
    return dist
    
time = []
from_x = dijkstra(X)
for i in range(1, N+1):
    time.append(dijkstra(i)[X]+from_x[i])
print(max(time))