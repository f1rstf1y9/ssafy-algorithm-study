import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF]*(n) for _ in range(n)]

for i in range(n):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)

for a in range(n): # 무조건 거쳐가는 노드
    for b in range(n): # b부터
        for c in range(n): #c까지
            graph[b][c] = min(graph[b][c], graph[b][a] + graph[a][c])
for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            graph[i][j] = 0
for g in graph:
    print(*g)