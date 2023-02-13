N, M = map(int, input().split())
visited = []
min_dist = 101*N*N

def get_dist(min_dist):
    dist = 0
    for h in houses:
        min_d = 101
        for i in range(len(check)):
            if check[i]:
                d = (abs(chickens[i][0]-h[0]) + abs(chickens[i][1]-h[1]))
                if min_d > d:
                    min_d = d
        dist += min_d
        if dist >= min_dist:
            return min_dist
    return dist if min_dist > dist else min_dist

def get_comb(idx, cnt):
    global min_dist
    if cnt == M:
        min_dist = get_dist(min_dist)
    if idx >= len(chickens):
        return
    check[idx] = 1
    get_comb(idx+1, cnt+1)
    check[idx] = 0
    get_comb(idx+1, cnt)

city = [list(map(int, input().split())) for _ in range(N)]
chickens, houses = [], []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chickens.append((i, j))
        if city[i][j] == 1:
            houses.append((i, j))
check = [0]*len(chickens)
get_comb(0, 0)
print(min_dist)