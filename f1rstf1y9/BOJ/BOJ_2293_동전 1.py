n, k = map(int, input().split())
value = [int(input()) for _ in range(n)]

dp = [(1 if i%value[0] == 0 else 0) for i in range(k+1)]

for i in range(1, n):
    temp = dp[:]
    v = value[i]
    for j in range(k+1):
        if j-v >= 0:
            temp[j] += temp[j-v]
    dp = temp
print(dp[k])