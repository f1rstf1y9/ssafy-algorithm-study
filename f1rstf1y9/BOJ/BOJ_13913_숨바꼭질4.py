from collections import deque
N, K = map(int, input().split())
time = [-1]*100001
def BFS(x):
    q = deque([x])
    time[x] = [0, -1]
    while q:
        x = q.popleft()
        if x == K:
            break
        for i in [x-1, x+1, 2*x]:
            if 0 <= i <= 100000 and time[i] == -1:
                time[i] = [time[x][0] + 1, x]
                q.append(i)
BFS(N)

i = K
ans = []
while time[i][1] != -1:
    ans.append(i)
    i = time[i][1]
print(time[K][0])
print(N,*ans[::-1])