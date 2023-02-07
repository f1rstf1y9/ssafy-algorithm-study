N, K = map(int, input().split())
n = input()
queue = []
k = K
for i in n:
    while queue and k and queue[-1] < i:
        queue.pop()
        k -= 1
    queue.append(i)
if len(queue) == N-K:
    print(''.join(queue))
else:
    print(''.join(queue[:N-K]))