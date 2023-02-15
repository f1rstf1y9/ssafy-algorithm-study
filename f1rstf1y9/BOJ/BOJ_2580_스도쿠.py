def fill(n):
    if n == len(zeros):
        return True
    x, y = zeros[n][0], zeros[n][1]
    c1 = sudoku[x]
    c2 = [sudoku[i][y] for i in range(9)]
    c3 = []
    for i in range(3):
        c3 += sudoku[x//3*3+i][y//3*3:y//3*3+3]
    for i in range(1, 10):
        if i not in c1 and i not in c2 and i not in c3:
            sudoku[x][y] = i
            if not fill(n+1):
                sudoku[x][y] = 0
            else:
                return True
    return False

sudoku = [list(map(int, input().split())) for _ in range(9)]
zeros = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zeros.append((i, j))
fill(0)
for s in sudoku:
    print(*s)


'''
1 3 5 4 6 9 2 7 8
7 8 2 1 3 5 6 4 9
4 6 9 2 7 8 1 3 5
3 2 1 5 4 6 8 9 7
8 7 4 9 1 3 5 2 6
5 9 6 8 2 7 4 1 3
9 1 7 6 5 2 3 8 4
6 4 3 7 8 1 9 5 2
2 5 8 3 9 4 7 6 1

1 3 5 4 6 0 2 0 8
7 0 2 1 3 5 6 4 9
4 6 9 2 7 8 1 3 5
3 2 1 5 4 6 8 0 7
8 0 4 9 0 3 5 2 6
5 9 6 8 0 7 4 1 3
0 1 7 6 5 2 3 8 4
6 4 3 7 8 1 0 5 2
2 5 8 3 0 4 7 6 1
'''