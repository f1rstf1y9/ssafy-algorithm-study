N = int(input())
liq = list(map(int, input().split()))
s, e = 0, N-1
min_v = 1e10
min_liq = []
while s<e:
    if abs(liq[s]+liq[e]) < min_v:
        min_v = abs(liq[s]+liq[e])
        min_liq = [liq[s], liq[e]]
    if abs(liq[s+1]+liq[e]) < abs(liq[s]+liq[e-1]):
        s += 1
    else:
        e -= 1
if 0 <= s+1 < N and 0 <= e+1 < N and abs(liq[s+1]+liq[e+1]) < min_v:
    print(liq[s+1], liq[e+1])
elif 0 <= s-1 < N and 0 <= e-1 < N and abs(liq[s-1]+liq[e-1]) < min_v:
    print(liq[s-1], liq[e-1])
else:
    print(*min_liq)