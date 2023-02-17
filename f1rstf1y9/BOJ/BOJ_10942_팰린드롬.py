import sys
input = sys.stdin.readline

N = int(input())
nums = [0] + list(map(int, input().split()))
M = int(input())
dp = [[0]*(N+1) for _ in range(N+1)]
quest = [[]*M]
max_len = 0
for i in range(1, N+1):
    dp[i][i] = 1
    if nums[i-1] == nums[i]:
        dp[i-1][i] = 1
for n in range(2, N):
    for s in range(1, N+1-n):
        if nums[s] == nums[s+n] and dp[s+1][s+n-1]:
            dp[s][s+n] = 1
for i in range(M):
    S, E = map(int, input().split())
    if E-S+1 > max_len:
        max_len = E-S+1
    quest.append()