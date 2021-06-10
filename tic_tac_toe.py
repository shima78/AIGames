import random


class TicTacToe:
    def __init__(self):
        self.ai = 'X'
        self.human = 'O'
        # Driver code
        self.board = [
            ['?', '?', '?'],
            ['?', '?', '?'],
            ['?', '?', '?']
        ]

    # start again
    def clean(self):
        self.ai = 'X'
        self.human = 'O'
        # Driver code
        self.board = [
            ['?', '?', '?'],
            ['?', '?', '?'],
            ['?', '?', '?']
        ]

    # show board
    def show(self):
        print('i/j  0     1     2')
        print('    ___   ___   ___ ')
        for i in range(0, 3):
            for j in range(0, 3):
                if j == 0:
                    print(' {} | {} |'.format(i, self.board[i][j]), end=" ")
                else:
                    print('| {} |'.format(self.board[i][j]), end=" ")
            print()
            print('    ___   ___   ___ ')
        print()

    # check anyone won or draw or game continues
    def evaluate(self):
        # horizontal
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '?':
                if self.board[i][0] == self.ai:
                    return 1
                else:
                    return -1
        # vertical
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '?':
                if self.board[0][i] == self.ai:
                    return 1
                else:
                    return -1
        # diagonal
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '?':
            if self.board[0][0] == self.ai:
                return 1
            else:
                return -1
        if self.board[2][0] == self.board[1][1] == self.board[0][2] != '?':
            if self.board[2][0] == self.ai:
                return 1
            else:
                return -1
        # not ended
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '?':
                    return None
        # draw
        return 0

    def maxPruning(self, depth, alpha, beta):
        e = self.evaluate()
        bestMove = (-1, -1)
        if e is not None:
            return e, (0, 0)

        v = -1000

        # Traverse all cells
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '?':
                    # Make the move and evaluate it
                    self.board[i][j] = self.ai
                    b = self.minPruning(depth + 1, alpha, beta)
                    if b > v:
                        v = b
                        alpha = max(v, alpha)
                        if depth == 0:
                            bestMove = (i, j)
                    # change back the move
                    self.board[i][j] = '?'

                    # prune
                    if v >= beta:
                        if depth == 0:
                            bestMove = (i, j)
                        return v, bestMove
        return v, bestMove

    def minPruning(self, depth, alpha, beta):
        e = self.evaluate()
        if e is not None:
            return e

        v = 1000

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '?':
                    # make a move and eval
                    self.board[i][j] = self.human
                    h, g = self.maxPruning(depth + 1, alpha, beta)
                    v = min(v, h)
                    beta = min(beta, v)
                    # change back the move
                    self.board[i][j] = '?'

                    # prune
                    if v <= alpha:
                        return v
        return v

    def pickStarter(self):
        a = random.randrange(10)
        if a % 2 == 0:
            return self.human
        return self.ai

    def play(self):
        turn = self.pickStarter()
        print(self.ai, "is AI and you are",self.human)
        print(turn, "plays first!")
        while True:
            self.show()
            e = self.evaluate()
            if e == 1:
                print("AI won!")
                return 1
            if e == -1:
                print(name, "won!")
                return -1
            if e == 0:
                print("Draw!")
                return 0
            if turn == self.human:
                row = input("enter number of row:\n")
                col = input("enter number of col:\n")
                row = int(row)
                col = int(col)
                if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == '?':
                    self.board[row][col] = self.human
                    turn = self.ai
                else:
                    print("invalid move! try another move")

            elif turn == self.ai:
                a, move = self.maxPruning(0, -1000, 1000)
                print(move)
                i = move[0]
                j = move[1]
                self.board[i][j] = self.ai
                print("AI made a move! human's turn")
                turn = self.human


if __name__ == "__main__":
    t = TicTacToe()
    name = input("enter your name: ")
    score_ai = 0
    score_human = 0
    counter = 0
    while True:
        t.clean()
        score = t.play()
        counter += 1
        if score == 1:
            score_ai += 1
        elif score == -1:
            score_human += 1
        print(str(counter) + " Games")
        print(name + "'s score: " + str(score_human))
        print("AI's score: " + str(score_ai))
        ans = input("wanna play again? y/n: ")
        if ans == 'n' or ans == 'N':
            break
