string = input()
bomb = list(input())
b_len = len(bomb)
k = 0
stack = []
for s in string:
    stack.append(s)
    if stack[len(stack)-b_len:] == bomb:
        for _ in range(b_len):
            stack.pop()
if stack:
    print(''.join(stack))
else:
    print('FRULA')