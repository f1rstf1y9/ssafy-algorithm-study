from collections import deque
T = int(input())
for _ in range(T):
    p = list(input())
    n = int(input())
    rev = False
    lst = deque(input()[1:-1].split(','))
    if lst[0] == '' and p[0] == 'D':
        print('error')
    else:
        for i in range(len(p)):
            if p[i] == 'R':
                rev = False if rev else True
            elif p[i] == 'D':
                if not lst or len(lst) == 1 and lst[0] == '':
                    print('error')
                    break
                else:
                    if rev:
                        lst.pop()
                    else:
                        lst.popleft()
        else:
            ans = ''
            if rev:
                lst = list(lst)[::-1]
            print('['+','.join(lst)+']')