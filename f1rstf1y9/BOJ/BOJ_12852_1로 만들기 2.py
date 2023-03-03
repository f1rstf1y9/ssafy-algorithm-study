N = int(input())
dp = [[0], [1], [2,1], [3,1]]
for i in range(4, N+1):
    temp = []
    if i%3 == 0:
        temp.append([i]+dp[i//3])
    if i%2 == 0:
        temp.append([i]+dp[i//2])
    temp.append([i]+dp[i-1])
    dp.append(min(temp, key=lambda x:len(x)))
print(len(dp[N])-1)
print(*dp[N])