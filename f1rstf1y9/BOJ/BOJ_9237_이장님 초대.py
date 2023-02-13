N = int(input())
t = list(map(int, input().split()))
t.sort(reverse=True)
cur_d, ans = 1, t[0]+1
for d in t:
    cur_d += 1
    if ans < cur_d+d:
        ans = cur_d+d
print(ans)