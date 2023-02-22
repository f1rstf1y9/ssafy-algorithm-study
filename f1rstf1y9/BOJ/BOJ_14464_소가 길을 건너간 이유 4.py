C, N = map(int, input().split())
T = sorted([int(input()) for _ in range(C)])
cows = [list(map(int, input().split())) for _ in range(N)]
visited = [0]*C
cows.sort(key=lambda x:(x[1], x[0]))
cnt = 0

for s, e in cows:
    for i in range(C):
        if s <= T[i] <= e and not visited[i]:
            cnt += 1
            visited[i] = 1
            break
        
print(cnt)