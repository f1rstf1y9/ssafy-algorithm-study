import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())
min_h = []
max_h = []
for _ in range(N):
    n = int(input().rstrip())
    if len(min_h) == len(max_h):
        heappush(max_h, -n)
    else:
        heappush(min_h, n)
    if min_h and min_h[0] < -max_h[0]:
        t1, t2 = -heappop(min_h), -heappop(max_h)
        heappush(min_h, t2)
        heappush(max_h, t1)
    print(-max_h[0])
