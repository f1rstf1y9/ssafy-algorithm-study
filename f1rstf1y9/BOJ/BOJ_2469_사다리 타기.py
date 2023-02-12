k, n, res = int(input()), int(input()), input()
top, btm, btm_num = [chr(65+i) for i in range(k)], ['' for i in range(k)], [i for i in range(k)]
cur = top
for m in range(n):
    l = input()
    if l[0] == '?':
        cur = btm_num
        continue
    for i in range(k-1):
        if l[i] == '-':
            cur[i], cur[i+1] = cur[i+1], cur[i]
for i in range(k):
    btm[btm_num[i]] = res[i]
ans = list('*'*(k-1))
for i in range(k-1):
    if top[i] == btm[i+1] and top[i+1] == btm[i]:
        ans[i] = '-'
        top[i],top[i+1] = top[i+1], top[i]
if top == btm:
    print(''.join(ans))
else:
    print('x'*(k-1))