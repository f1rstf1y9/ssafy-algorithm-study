N = int(input())
p_lst = []
m_lst = []
for _ in range(N):
	n = int(input())
	if n > 0:
		p_lst.append(n)
	else:
		m_lst.append(n)
p_lst.sort(reverse=True)
m_lst.sort()
origin_sum = sum(p_lst)+sum(m_lst)
sum_v = 0

for i in range(0, len(p_lst), 2):
	if i+1 < len(p_lst):
		a = p_lst[i]+p_lst[i+1]
		b = p_lst[i]*p_lst[i+1]
		sum_v += max(a, b)
	else:
		sum_v += p_lst[i]

for i in range(0, len(m_lst), 2):
	if i+1 < len(m_lst):
		sum_v += m_lst[i]*m_lst[i+1]
	else:
		sum_v += m_lst[i]
print(max(origin_sum, sum_v))