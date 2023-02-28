import sys
input = sys.stdin.readline
lines = []
N = int(input().rstrip())
lines = [list(map(int, input().split())) for _ in range(N)]
lines.sort(key=lambda x:x[0])
complete_line = []
for l in lines:
	for i in range(len(complete_line)):
		c = complete_line[i]
		if c[0] <= l[0] and c[1] >= l[0]:
			c[1] = max(c[1],l[1])
			break
	else:
		complete_line.append(l)
ans = 0
for c in complete_line:
	ans += (c[1]-c[0])
print(ans)