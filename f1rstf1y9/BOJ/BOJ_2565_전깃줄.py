N = int(input())
wires = []
for _ in range(N):
    wires.append(tuple(map(int, input().split())))
wires.sort()
dp = [1]*N
ans = 0
for i in range(1,N):
    for j in range(i):
        if wires[i][1] > wires[j][1]:
            if dp[j] >= dp[i]:
                dp[i] = dp[j]+1
    ans = max(ans, dp[i])
print(N-ans)
