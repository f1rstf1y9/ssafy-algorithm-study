string = [0]+list(input())
N = len(string)-1
dp = [[0]*(N+1) for _ in range(N+1)]

palin_list = []
for i in range(1, N+1):
    dp[i][i] = 1
    if string[i-1] == string[i]:
        dp[i-1][i] = 1
for n in range(2, N):
    for s in range(1, N+1-n):
        if string[s] == string[s+n] and dp[s+1][s+n-1]:
            dp[s][s+n] = 1

set_dp = [i for i in range(N+1)]

for i in range(1, N+1):
    set_dp[i] = set_dp[i-1]+1
    for j in range(i):
        if dp[j][i]:
            if j == 1:
                set_dp[i] = 1
                break
            if set_dp[i] > set_dp[j-1] + 1:
                set_dp[i] = set_dp[j-1] + 1
print(set_dp[N])