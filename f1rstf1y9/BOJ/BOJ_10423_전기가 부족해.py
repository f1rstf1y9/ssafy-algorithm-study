import sys
input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split())
parent = [i for i in range(N+1)]
pw_plant = [0]*(N+1)
temp = [[] for _ in range(N+1)]
for i in map(int, input().rstrip().split()):
    pw_plant[i] = 1
edges = [list(map(int, input().rstrip().split())) for _ in range(M)]
edges.sort(key=lambda x:x[2])

cost = 0
while sum(pw_plant) != N:
    for edge in edges:
        if pw_plant[edge[0]] and pw_plant[edge[1]]:
            continue
        if (pw_plant[edge[0]] or pw_plant[edge[1]]):
            pw_plant[edge[0]] = pw_plant[edge[1]] = 1
            cost += edge[2]
            break
print(cost)