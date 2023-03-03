from heapq import heappop, heappush
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(N)]
bags = sorted([int(input()) for _ in range(K)])

j_heap = []
for m, v in jewels:
    heappush(j_heap, (-v, m))
ans = 0
for b in bags:
    temp = []
    while b < j_heap[0][1]:
        temp.append(heappop(j_heap))
    if j_heap:
        ans += heappop(j_heap)[0]
    else:
        break
print(-ans)
