import sys
sys.setrecursionlimit(10**6)

def dfs(n):
    global cnt
    visited[n] = 1
    history.append(n)
    if visited[nums[n]]:
        if nums[n] in history:
            cnt -= len(history[history.index(nums[n]):])
        return
    else:
        dfs(nums[n])

T = int(input())
for _ in range(T):
    N = int(input())
    nums = [0]+list(map(int, input().split()))
    visited = [0]*(N+1)
    cnt = N
    for i in range(1,N+1):
        if not visited[i]:
            history = []
            dfs(i)
    print(cnt)
