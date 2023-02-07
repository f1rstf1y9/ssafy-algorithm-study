from heapq import heappop, heappush, heapify
import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    C = list(map(int, input().split()))
    if N == 1:
        print(1)
        continue
    heapify(C)
    total = []
    while len(C) != 1:
        a, b = heappop(C), heappop(C)
        total.append(a*b)
        heappush(C, a*b)
    ans = 1
    for i in total:
        ans *= i
    print(ans % 1000000007)