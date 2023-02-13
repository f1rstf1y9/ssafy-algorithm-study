from heapq import heappop, heappush
import sys
input = sys.stdin.readline
N = int(input())
times = [tuple(map(int, input().split())) for _ in range(N)]
times.sort(key=lambda x:(x[0],x[1]))
rooms = []
heappush(rooms, times[0][1])
times = times[1:]
for t in times:
    if rooms[0] <= t[0]:
        heappop(rooms)
    heappush(rooms, t[1])
print(len(rooms))