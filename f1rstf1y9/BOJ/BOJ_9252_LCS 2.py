str1 = input()
str2 = input()
l1, l2 = len(str1), len(str2)
dp = [[(0, '')]*(l2+1) for _ in range(l1+1)]

for i in range(1, l1+1):
    for j in range(1, l2+1):
        if str1[i-1] == str2[j-1]:
            x = dp[i-1][j-1]
            dp[i][j] = (x[0]+1, x[1]+str1[i-1])
        else:
            x, y = dp[i-1][j], dp[i][j-1]
            if x[0] >= y[0]:
                dp[i][j] = (x[0], x[1])
            else:
                dp[i][j] = (y[0], y[1])

print(dp[l1][l2][0])
print(dp[l1][l2][1])
