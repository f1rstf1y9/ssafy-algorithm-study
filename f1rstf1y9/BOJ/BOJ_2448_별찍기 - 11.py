N = int(input())
line = ['  *  ', ' * * ', '*****']
def recur(depth):
    if 3*2**depth == N:
        for i in range(N):
            print(line[i])
        return
    for i in range(3*2**depth):
        line.append(line[i] + ' ' + line[i])
        line[i] = ' ' * (3*2**depth) + line[i] + ' ' * (3*2**depth)
    recur(depth + 1)
recur(0)