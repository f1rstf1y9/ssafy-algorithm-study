def get_parent(cost):
    if parent[cost] != cost:
        parent[cost] = get_parent(parent[cost])
    return parent[cost]

def union(cost1, cost2):
    a = get_parent(cost1)
    b = get_parent(cost2)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
cost_map = [list(map(int, input().split())) for _ in range(N)]
costs = []
parent = [i for i in range(N+1)]
for i in range(N):
    for j in range(i+1, N):
        costs.append((cost_map[i][j], i+1, j+1))
costs.sort()
ans = 0
for cost in costs:
    if get_parent(cost[1]) != get_parent(cost[2]):
        union(cost[1], cost[2])
        ans += cost[0]
print(ans)