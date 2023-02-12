N, M = map(int,input().split())
lst = []
visited = []
def dfs():
    if len(lst) == M and set(lst) not in visited:
        visited.append(set(lst))
        print(*lst)
        return
    for i in range(1, N+1):
        if i not in lst:
            lst.append(i)
            dfs()
            lst.pop()
dfs()