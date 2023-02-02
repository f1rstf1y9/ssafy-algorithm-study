from heapq import heappop, heappush
import sys

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if heap:
            print(-1*heappop(heap))
        else:
            print(0)
    else:
        heappush(heap, -x)