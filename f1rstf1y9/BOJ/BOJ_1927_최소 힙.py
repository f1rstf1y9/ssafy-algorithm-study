from heapq import heappop, heappush
import sys
input = sys.stdin.readline
N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x == 0:
        print(heappop(heap) if heap else 0)
    else:
        heappush(heap, x)