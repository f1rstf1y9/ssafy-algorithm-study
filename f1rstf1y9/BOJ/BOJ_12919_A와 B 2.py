S = input()
T = input()

lst = [T]
for _ in range(len(T)-len(S)):
    new_lst = []
    for l in lst:
        if l[0] == 'B':
            new_lst.append(str(l[1:][::-1]))
        if l[-1] == 'A':
            new_lst.append(str(l[:-1]))
    lst = new_lst
if S in lst:
    print(1)
else:
    print(0)