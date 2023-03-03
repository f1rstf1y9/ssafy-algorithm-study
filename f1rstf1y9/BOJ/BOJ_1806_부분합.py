N, S = map(int, input().split())
lst = list(map(int, input().split()))
min_lst = N+1
total = 0
s = e = 0
for s in range(N):
    while total < S and e < N:
        total += lst[e]
        e += 1
    if total >= S and min_lst > e-s:
        min_lst = e-s
    total -= lst[s]
if min_lst == N+1:
    print(0)
else:
    print(min_lst)