N, K = map(int, input().split())
t = 0
now = [N]
visited = [0] * 100001
while t <= abs(N-K):
    if K in now:
        break
    next = []
    t += 1
    for n in now:
        for i in [n-1, n+1, 2*n]:
            if 0 <= i <= 100000 and not visited[i]:
                next.append(i)
                visited[i] = 1
    now = next
print(t)