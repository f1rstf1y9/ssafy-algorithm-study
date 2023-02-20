valids = []
def isGameOver(board):
    for i in range(3):
        if ''.join(board[i*3:i*3+3]) in ['OOO', 'XXX']:
            return True
        if ''.join(board[i:i+7:3]) in ['OOO', 'XXX']:
            return True
    if board[0]+board[4]+board[8] in ['OOO', 'XXX'] or board[2]+board[4]+board[6] in ['OOO', 'XXX']:
        return True
    return False

def game(n):
    if n == 9:
        valids.append(''.join(board))
        return
    for i in range(9):
        if board[i] == '.':
            board[i] = 'O' if n%2 else 'X'
            if isGameOver(board):
                valids.append(''.join(board))
            else:
                game(n+1)
            board[i] = '.'

board = ['.']*9
game(0)

while True:
    ttt = input()
    if ttt == "end":
        break
    if ttt in valids:
        print("valid")
    else:
        print("invalid")