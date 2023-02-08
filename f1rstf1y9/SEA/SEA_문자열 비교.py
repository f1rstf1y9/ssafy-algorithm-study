T = int(input())
def is_sub(pat, s):
    i = 0
    p = len(pat)
    pat = pat[::-1]
    while i <= len(s)-p:
        chk = s[i:i+p][::-1]
        print(chk[::-1])
        for j in range(p):
            if chk[j] != pat[j]:
                if chk[j] in pat:
                    i += pat.index(chk[j])-j
                else:
                    i += p-j
                break
        else:
            return 1
    return 0
for t in range(T):
    a = input()
    b = input()
    print(f"#{t+1}", end=' ')
    print(1 if is_sub(a,b) else 0)