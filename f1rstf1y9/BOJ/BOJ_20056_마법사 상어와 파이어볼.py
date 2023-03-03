direct = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def make_move(fbs):
    new_fbs = {}
    for fb in fbs:
        for f in fbs[fb]:
            ny, nx = (fb[0]+direct[f[2]][0]*f[1])%N, (fb[1]+direct[f[2]][1]*f[1])%N
            if (ny, nx) in new_fbs:
                new_fbs[(ny, nx)].append(f)
            else:
                new_fbs[(ny, nx)] = [f]
    return new_fbs

def div_fb(fbs):
    new_fbs = {}
    for fb in fbs:
        if len(fbs[fb]) >= 2:
            m = s = 0
            d = set()
            for f in fbs[fb]:
                m += f[0]
                s += f[1]
                d.add(f[2]%2)
            if m//5 != 0:
                if len(d) == 1:
                    d = [0,2,4,6]
                else:
                    d = [1,3,5,7]
                for i in d:
                    if fb in new_fbs:
                        new_fbs[fb].append((m//5, s//len(fbs[fb]), i))
                    else:
                        new_fbs[fb] = [(m//5, s//len(fbs[fb]), i)]
        else:
            new_fbs[fb] = fbs[fb]
    return new_fbs

N, M, K = map(int, input().split())
fbs = {}
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fbs[(r-1,c-1)] = [(m, s, d)]

for _ in range(K):
    fbs = make_move(fbs)
    fbs = div_fb(fbs)
ans = 0
for fb in fbs:
    for f in fbs[fb]:
        ans += f[0]
print(ans)