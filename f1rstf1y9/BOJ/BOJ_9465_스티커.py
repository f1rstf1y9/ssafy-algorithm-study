import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    sti = []
    for _ in range(2):
        sti.append(list(map(int, input().split())))
    dp = [[sti[0][0], sti[1][0]]]
    if n > 1:
        dp.append([dp[0][1]+sti[0][1], dp[0][0]+sti[1][1]])
    if n > 2:
        for i in range(2, n):
            dp.append([max(dp[i-2][0], dp[i-2][1], dp[i-1][1])+sti[0][i],
            max(dp[i-2][0], dp[i-2][1], dp[i-1][0])+sti[1][i]])
    print(max(dp[n-1]))