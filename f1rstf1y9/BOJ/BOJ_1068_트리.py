N = int(input())
tree = list(map(int, input().split()))
remain = [i for i in range(N)]
child = [[] for i in range(N)]
q = [int(input())]
for i in range(N):
    if tree[i] != -1:
        child[tree[i]].append(i)
while q:
    p = q.pop()
    if p != -1:
        remain.remove(p)
        for i in range(len(child[p])):
            if tree[child[p][i]] != -1:
                q.append(child[p][i])
    child[p].clear()
ans = 0
for i in remain:
    if not child[i]:
        ans += 1
    else:
        for c in child[i]:
            if c in remain:
                break
        else:
            ans += 1
print(ans)