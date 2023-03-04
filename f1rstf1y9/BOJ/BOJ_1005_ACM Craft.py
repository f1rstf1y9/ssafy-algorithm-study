'''메인아이디어
주어진 도착 건물부터 시작하여 시작점까지 찾아가기
'''

from collections import deque
import sys
input = sys.stdin.readline

def bfs(n):
    q = deque([n])
    t_time[n] = time[n]
    while q:
        p = q.popleft()
        # 더이상 먼저 건설해야하는 건물이 없으면 출발 건설로 보고 finish에 저장
        if not graph[p]:
            finish.append(p)
        # 먼저 건설해야하는 건물(i)이 있을 떄
        for i in graph[p]:
            # 현재 해당 건물(i)까지 건설하는데 걸리는 시간으로 저장된 것보다,
            # 그 이후 건물(p)를 건설하는데 걸리는 시간 + i하나를 건설하는 시간이 더 크면 갱신
            if t_time[i] < t_time[p]+time[i]:
                t_time[i] = t_time[p]+time[i]
                q.append(i)

T = int(input()) # 테케 수
for _ in range(T):
    N, K = map(int, input().split()) # 건물 개수, 건설순서 규칙 수
    graph = [[] for i in range(N+1)] # 간선 정보
    time = [0]+list(map(int, input().split())) # 건물 하나 짓는 데 걸리는 시간
    t_time = [0]*(N+1) # 도착 건물로부터 각 출발 건물까지 걸리는 시간들

    # 간선 정보 저장하기
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y].append(x)

    # 도착 건물 출발 건물 입력받기
    W = int(input())
    finish = []
    bfs(W)
    max_finish = 0
    for f in finish:
        if t_time[f] > max_finish:
            max_finish = t_time[f]
    print(max_finish)
