from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())
time = []
for i in range(N):
    time.append(list(map(int, input().split())))
time.sort(key=lambda x: (x[0], x[1]))
class_heap = [time[0][1]]
for i in range(1, N):
    if class_heap[0] <= time[i][0]:
        heappop(class_heap)
        heappush(class_heap, time[i][1])
    else:
        heappush(class_heap, time[i][1])
print(len(class_heap))