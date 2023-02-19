ans = 0
def dfs(n):
    global ans
    if n == N:
        ans += 1
    else:
        for i in range(N):
            if i in stack:
                continue
            for j in range(1, n+1):
                if stack[n-j] == i-j or stack[n-j] == i+j:
                    break
            else:
                stack.append(i)
                dfs(n+1)
                stack.pop()
N = int(input())
stack = []
dfs(0)
print(ans)