n=int(input())
a=list(map(int,input().split()))

dp = [[[a[i]] for i in range(n)] for i in range(n)]
ans_l = 1
ans_w = dp[0][0]

for i in range(1,n): #length
    temp = []
    for j in range(n): #position
        if j < i:
            temp.append(dp[i-1][j])
        else:
            for k in range(j):
                cur = dp[i-1][k]
                if len(cur) == i and cur[-1] < a[j]:
                    temp.append(cur+[a[j]])
                    ans_l, ans_w = i+1, temp[-1] 
                    break
            else:
                temp.append(dp[i-1][j])
    if dp[i-1] == temp:
        break
    dp[i] = temp
print(ans_l)
print(*ans_w)