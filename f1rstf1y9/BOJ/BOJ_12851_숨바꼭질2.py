from collections import deque

N, K = map(int, input().split())
time = [-1]*100001
cnt = 0

def BFS(x):
    global cnt	
    queue = deque([N])
    time[N] = 0

    while queue:
        x = queue.popleft()
        if x == K:
            cnt += 1
        for i in (x-1, x+1, 2*x):
            if 0 <= i <= 100000 and (time[i]==-1 or time[i] == time[x]+1):
                time[i] = time[x] + 1
                queue.append(i)
                
BFS(N)
print(time[K])
print(cnt)