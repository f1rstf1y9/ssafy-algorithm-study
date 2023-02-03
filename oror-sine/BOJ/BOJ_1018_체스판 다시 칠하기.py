WChess = ["BWBWBWBW" if i%2 else "WBWBWBWB" for i in range(8)]
BChess = ["WBWBWBWB" if i%2 else "BWBWBWBW" for i in range(8)]

M, N = map(int, input().split())
board = [input() for _ in range(M)]

repaint = 64
for m in range(M-7):
    for n in range(N-7):
        Ws = Bs = 0
        for row, Wrow, Brow in zip(board[m:m+8], WChess, BChess):
            for col, Wcol, Bcol in zip(row[n:n+8], Wrow, Brow):
                Ws += 0 if col == Wcol else 1
                Bs += 0 if col == Bcol else 1
        minimum = Ws if Ws<=Bs else Bs
        if minimum<repaint: repaint = minimum

print(repaint)