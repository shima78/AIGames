import random
import time


class NQueens:
    def __init__(self, n):
        self.board = [['_'] * n for i in range(n)]
        self.size = n
        self.conflict_flag = True
    def place_queens(self):
        # put 1 queen in each row
        for i in range(self.size):
            j = random.randrange(self.size)
            self.board[i][j] = 'Q'


    # pick a random queen
    def pick_queen(self):
        queenPos = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 'Q':
                    c = self.count_conflicts(i, j)
                    if c>0:
                        queenPos.append((i, j))
        p = random.randrange(len(queenPos))
        return queenPos[p]

    # count number of conflicts of a queen
    def count_conflicts(self, row, col):
        count = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 'Q' and not (row == i and col == j):
                    # horizontal attack
                    if i == row:
                        count += 1

                    # vertical attack
                    elif j == col:
                        count += 1

                    #  diagonal attack
                    elif abs(row - i) == abs(col - j):
                        count += 1
        return count

    def is_solved(self):
        self.conflict_flag = True
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == 'Q':

                    for i in range(self.size):
                        for j in range(self.size):

                            if self.board[i][j] == 'Q' and not (row == i and col == j):
                                # horizontal attack
                                if i == row:
                                    return False

                                # vertical attack
                                elif j == col:
                                    return False


                                #  diagonal attack
                                elif abs(row - i) == abs(col - j):
                                    return False

        return True

    def min_conflict_solver(self):
        start = time.time()
        iterations = 0
        total_iterations = 0
        while not self.is_solved():
            iterations += 1
            total_iterations += 1
            if iterations > 50 + self.size*2:
                print("going again!")
                iterations = 0
                self.board = [['_'] * self.size for i in range(self.size)]
                self.place_queens()
            # minimizing the attacks
            attacks = self.size + 1
            q = self.pick_queen()
            minConflictedMove = (-1, -1)
            i = q[0]
            for j in range(self.size):
                if self.board[i][j] == '_':
                    # move
                    self.board[q[0]][q[1]] = '_'
                    self.board[i][j] = 'Q'
                    countedConflicts = self.count_conflicts(i, j)
                    if countedConflicts < attacks:
                        minConflictedMove = (i, j)
                        attacks = countedConflicts
                    # undo move
                    self.board[i][j] = '_'
                    self.board[q[0]][q[1]] = 'Q'
            # move to best position
            self.board[q[0]][q[1]] = '_'
            self.board[minConflictedMove[0]][minConflictedMove[1]] = 'Q'

        end = time.time()
        print("duration : ", end - start, "\niterations: ", iterations, "\ntotal iterations: ", total_iterations)
        self.show_board()

    def show_board(self):
        for i in range(self.size):
            for j in range(self.size):

                if j == 0:
                    print('| {} |'.format(self.board[i][j]), end=" ")
                else:
                    print('{} |'.format(self.board[i][j]), end=" ")
            print()


size = input("enter size of board : ")
q = NQueens(int(size))
q.place_queens()
q.min_conflict_solver()
