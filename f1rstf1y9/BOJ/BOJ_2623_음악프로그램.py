from collections import deque

N, M = map(int,input().split())
nodes = [[] for _ in range(N+1)]
enter_len = [0]*(N+1)

for _ in range(M):
    pd = list(map(int, input().split()))
    n, ord = pd[0], pd[1:]
    for i in range(n - 1):
        if ord[i] not in nodes[ord[i+1]]:
            nodes[ord[i]].append(ord[i+1])
            enter_len[ord[i+1]] += 1

q = deque([])
for i in range(1,N+1):
    if not enter_len[i]:
        q.append(i)
ans = []
while q:
    p = q.pop()
    ans.append(p)
    for i in nodes[p]:
        enter_len[i] -= 1
        if not enter_len[i]:
            q.append(i)
if len(ans) != N:
    print(0)
else:
    print(*ans, sep='\n')

'''
왜 안되지
def dfs(i):
    for n in nodes[i]:
        if n in history:
            print("False")
            return False
        else:
            history.append(n)
            dfs(n)
            history.pop()
    return True

'''