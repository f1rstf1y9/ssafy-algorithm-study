N, M = map(int, input().split())
know = input().split()
party = []

def dfs(p):
    stack = [p]
    while stack:
        now = stack.pop()
        for p in party:
            if not p[0]:
                for n in now:
                    if n in p[1]:
                        p[0] = True
                        stack.append(p[1])

if know != '0':
    know = list(map(int, know))[1:]
else:
    know = []

for _ in range(M):
    p = list(map(int, input().split()))[1:]
    say = False
    for n in p:
        if n in know:
            say = True
            break
    party.append([say, p])

for p in party:
    if p[0]:
        dfs(p[1])
if know == '0':
    print(M)
else:
    ans = 0
    for p in party:
        if not p[0]:
            ans += 1
    print(ans)