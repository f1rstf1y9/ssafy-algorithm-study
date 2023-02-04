import sys
input = sys.stdin.readline
N = int(input())
lst = [list(map(int, input().rstrip().split())) for _ in range(N)]
lst = sorted(lst, key=lambda x:(x[1],x[0]))
end = lst[0][1]
cnt = 1
for n in lst[1:]:
    if n[0] >= end:
        end = n[1]
        cnt += 1
print(cnt)