import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

lst = []
cnt = 0
for i in range(N):
    if not lst or lst[-1] < A[i]:
        lst.append(A[i])
        cnt += 1
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
print(cnt)