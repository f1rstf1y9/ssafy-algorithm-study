from heapq import heappop, heappush
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    min_heap = []
    max_heap = []
    k = int(input())
    visited = [False]*k
    for i in range(k):
        calc, n = input().split()
        if calc == 'I':
            heappush(min_heap, (int(n), i))
            heappush(max_heap, (-int(n), i))
        elif calc == 'D':
            if min_heap and n == '-1':
                while min_heap and visited[min_heap[0][1]]:
                    heappop(min_heap)
                if min_heap:
                    visited[heappop(min_heap)[1]] = True
            if max_heap and n == '1':
                while max_heap and visited[max_heap[0][1]]:
                    heappop(max_heap)
                if max_heap:
                    visited[heappop(max_heap)[1]] = True
    while min_heap and visited[min_heap[0][1]]:
        heappop(min_heap)
    while max_heap and visited[max_heap[0][1]]:
        heappop(max_heap)
    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")