from collections import deque
N, K = map(int, input().split())
time = [-1]*100001

def BFS(x):
    q = deque([x])
    time[x] = 0
    
    while q:
        x = q.popleft()
        if x == K:
            break
        if 0 <= 2*x <= 100000 and time[2*x] == -1:
            time[2*x] = time[x]
            q.append(2*x)
        for i in [x-1, x+1]:
            if 0 <= i <= 100000 and time[i] == -1:
                time[i] = time[x]+1
                q.append(i)
                
BFS(N)
print(time[K])