from heapq import heappop, heappush
import sys
input = sys.stdin.readline
N = int(input())
q = []
ans = []
for _ in range(N):
    heappush(q, int(input()))
while len(q) != 1:
    n = heappop(q)+heappop(q)
    ans.append(n)
    heappush(q, n)
print(sum(ans))

