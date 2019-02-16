# My approach to this problem is that first we need to create an empty tic-tac-toe
# board using a list of lists of empty strings. Each time a player makes a move via
# the move function, we should check the positions to see if that player has won, 
# otherwise return 0.

class TicTacToe:

    def __init__(self, n=3):

        # initialize an board of n x n with empty spaces
        # the spaces will be useful in the move function
        # when we use ord() and math to see who has won
        self.board = [[" "] * n for i in range(n)]

        # initialize a status of if the game has been won
        self.status = 0

    def print(self):
        '''print prints the board in an easy to read format'''
        for row in self.board:
            print(row)
        print()

    def move(self, x, y, p):

        # place the move on the board
        if p == 1:
            self.board[x][y] = "X"
        else:
            self.board[x][y] = "O"

        # check positions to see if p has won
        # there are 8 ways to win tic-tac-toe
        # if p has won, return 1
        # ord("X") = 88, ord("O") = 79, ord(" ") = 32
        # we will sum the 8 posible scenarios for winning
        sums = [0] * 8
        for i in range(3):
            sums[0] += ord(self.board[0][i])
        for i in range(3):
            sums[1] += ord(self.board[1][i])
        for i in range(3):
            sums[2] += ord(self.board[2][i])
        for i in range(3):
            sums[3] += ord(self.board[i][0])
        for i in range(3):
            sums[4] += ord(self.board[i][1])
        for i in range(3):
            sums[5] += ord(self.board[i][2])
        for i in range(3):
            sums[6] += ord(self.board[i][i])
        for i in range(2,-1,-1):
            sums[7] += ord(self.board[i][i])
        
        # if the sum divided by 3 is equal to the ord()
        # for the player's letter, that player has won
        for sum in sums:
            if p == 1 and sum // 3 == 88:
                self.status = 1
                return 1
            if p == 2 and sum // 3 == 79:
                self.status = 1
                return 1

        # return 0 as a default
        return 0
    
## TEST ##
moves = [
    (0, 0, 1),
    (0, 2, 2),
    (2, 2, 1),
    (1, 1, 2),
    (2, 0, 1),
    (1, 0, 2),
    (2, 1, 1)
]
toe = TicTacToe(3)
for move in moves:
    result = toe.move(move[0], move[1], move[2])
    toe.print()
    if result == 1:
        print("Player", move[2], "wins!")
        break