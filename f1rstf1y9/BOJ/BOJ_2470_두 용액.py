N = int(input())
liq = list(map(int, input().split()))
s_liq = [x for x in sorted(liq) if x > 0]
a_liq = [x for x in sorted(liq) if x < 0]
if len(s_liq) == N:
    print(s_liq[0], s_liq[1])
elif len(a_liq) == N:
    print(a_liq[-2], a_liq[-1])
else:
    min_v, min_1, min_2 = abs(s_liq[0]+a_liq[-1]), a_liq[-1], s_liq[0] 
    find = False
    for sl in s_liq:
        s, e = 0, len(a_liq)-1
        m = (s+e) // 2
        while s <= e:
            if min_v > abs(sl+a_liq[m]):
                min_v, min_1, min_2 = abs(sl + a_liq[m]), a_liq[m], sl
            if min_v == 0:
                find = True
                break
            if sl + a_liq[m] > 0:
                e = m-1
                m = (s + e)//2
            elif sl + a_liq[m] < 0:
                s = m+1
                m = (s + e)//2
        if find:
            break

    if len(s_liq) > 1:
        s_min = abs(s_liq[0] + s_liq[1])
        if s_min < min_v:
            min_1, min_2 = s_liq[0], s_liq[1]
    if len(a_liq) > 1:
        a_min = abs(a_liq[-2] + a_liq[-1])
        if a_min < min_v:
            min_1, min_2 = a_liq[-2], a_liq[-1]
    
    print(min_1, min_2)