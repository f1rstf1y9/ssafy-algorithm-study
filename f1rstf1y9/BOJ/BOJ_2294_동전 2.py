n, k = map(int, input().split())
value = [int(input()) for _ in range(n)]

dp = [[(i//value[0] if i%value[0] == 0 else 10001) for i in range(k+1)]]
for i in range(1, n):
    temp = dp[i-1][:]
    v = value[i]
    for j in range(k+1):
        c1 = c2 = 10001
        if j%v == 0:
            c1 = j//v
        if j-v >= 0 and temp[j-v] != 10001:
           c2 = temp[j-v] + 1
        temp[j] = min(c1,c2,temp[j])
    dp.append(temp)
if dp[-1][k] < 10001:
    print(dp[-1][k])
else:
    print(-1)