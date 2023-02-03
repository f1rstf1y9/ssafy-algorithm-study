import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    cmd = tuple(input().split())

    if cmd[0] == "push_front":
        stack = [cmd[1]] + stack

    elif cmd[0] == "push_back":
        stack.append(cmd[1])

    elif cmd[0] == "pop_front":
        print(stack.pop(0) if len(stack) else -1)

    elif cmd[0] == "pop_back":
        print(stack.pop() if len(stack) else -1)

    elif cmd[0] == "size":
        print(len(stack))

    elif cmd[0] == "empty":
        print(0 if len(stack) else 1)

    elif cmd[0] == "front":
        print(stack[0] if len(stack) else -1)

    elif cmd[0] == "back":
        print(stack[-1] if len(stack) else -1)
