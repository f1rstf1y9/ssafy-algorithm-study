def recur(lst, depth):
    if depth == M:
        print(*lst)
    for i in range(1, N+1):
        if i not in lst:
            recur(lst+[i], depth+1)
N, M = map(int, input().split())
for i in range(1, N+1):
    recur([i], 1)