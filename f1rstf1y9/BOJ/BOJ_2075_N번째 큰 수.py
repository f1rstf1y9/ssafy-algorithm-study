from heapq import heappop, heappush
N = int(input())
heap = []

for _ in range(N):
    for i in list(map(int, input().split())):
        heappush(heap, i)
        if len(heap) > N:
            heappop(heap)
print(heappop(heap))
'''

3
1 2 3
4 5 6
7 8 9

'''