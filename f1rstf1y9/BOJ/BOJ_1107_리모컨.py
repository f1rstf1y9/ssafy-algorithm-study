N = int(input())
M = int(input())
err = []
click = abs(N-100)

if M:
    err = input().split()

if len(err) == 10:
    print(click)
elif click == 0:
    print(0)
else:
    low = high = click
    for i in range(N, -1, -1):
        for n in str(i):
            if n in err:
                break
        else:
            now = len(str(i)) + N - i
            if now < low:
                low = now
    for i in range(N, N + click):
        for n in str(i):
            if n in err:
                break
        else:
            now = len(str(i)) + i - N
            if now < high:
                high = now
    print(min(click, low, high))
