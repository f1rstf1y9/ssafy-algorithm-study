import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

lst = []
P = [-1]*N
cnt = 0
for i in range(N):
    if not lst or lst[-1] < A[i]:
        lst.append(A[i])
        cnt += 1
        P[i] = cnt-1
    else:
        l, r = 0, cnt
        m = (r+l)//2
        while l < r:
            if lst[m] > A[i]:
                r = m
            elif lst[m] == A[i]:
                break
            else:
                l = m+1
            m = (r+l)//2
        lst[m] = A[i]
        P[i] = m
    
print(cnt)
i = N-1
ans = [-1]*cnt
cnt -= 1
while(cnt>=0):
    if P[i] == cnt:
        ans[cnt] = A[i]
        cnt -= 1
    i -= 1
print(*ans)