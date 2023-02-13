from heapq import heappush, heappop
import sys
input = sys.stdin.readline
N = int(input())
class_lst = [tuple(map(int, input().split())) for _ in range(N)]
class_lst.sort(key=lambda x:(x[1],x[2]))
heap = []
heappush(heap, [class_lst[0][2],class_lst[0][0]])
class_lst = class_lst[1:]
for c in class_lst:
    if heap[0][0] <= c[1]:
        heappush(heap, [c[2],c[0]]+heappop(heap))
    else:
        heappush(heap, [c[2],c[0]])
print(len(heap))
ans = [0]*N
cnt = 1
for h in heap:
    for i in range(len(h)//2):
        ans[h[i*2+1]-1] = cnt
    cnt += 1
print(*ans, sep='\n')
