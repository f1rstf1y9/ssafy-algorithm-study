def calc(stack):
    res = 0
    a = []
    for s in stack:
        a.append(A[s])

    for i in range(N-1):
        res += abs(a[i]-a[i+1])
    return res

def dfs(n):
    global ans
    if n == N:
        v = calc(stack)
        if v > ans:
            ans = v
    for i in range(N):
        if i not in stack:
            stack.append(i)
            dfs(n+1)
            stack.pop()

N = int(input())
A = list(map(int,input().split()))
stack = []
ans = 0
dfs(0)
print(ans)