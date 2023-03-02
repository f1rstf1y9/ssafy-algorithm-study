'''
 처음엔 모든 경우의 수 조사 ->set()를 만들어진 경우 리스트에 추가
 경우의수마다 만들어진 경우 리스트에 존재 유무 판단해서 calc()실행 여부 판단
 => dfs에서 idx 인자를 추가해서 중복되는 경우의 수 없도록 수정
'''

def calc():
    power_1 = 0
    power_2 = 0
    for i in range(N):
        for j in range(i+1, N):
            if visited[i] and visited[j]:
                power_1 += (S[i][j] + S[j][i])
            elif not (visited[i] or visited[j]):
                power_2 += (S[i][j] + S[j][i])
    return abs(power_1-power_2)

def dfs(n, idx):
    if n == N//2:
        power_d_lst.append(calc())
        return
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = 1
            dfs(n+1, i+1)
            visited[i] = 0

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
visited = [0]*N
visited[0] = 1
power_d_lst = []
dfs(1, 0)
print(min(power_d_lst))