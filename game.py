from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
import time
import math

class TicTacToe:
    def __init__(self) -> None:
        self.board =  self.make_board()#using a single list to represent a 3x3 board; not sure why
        self.current_winner = None
    
    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def available_moves(self):
        return [i for i,spot in enumerate(self.board) if spot==' ']
    
    def empty_squares(self):
        if ' ' in self.board:
            return True
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, letter, square):
        #if it is a valid move, add it to the board 
        if self.board[square]==' ':
            self.board[square] = letter
            if self.winner(letter,square):
                self.current_winner = letter
            return True
        return False
    
    def winner(self,letter,square):
        # Check all rows and columns
        row_index = math.floor(square/3)
        row = self.board[row_index*3:(row_index+1)*3]
        if all(s==letter for s in row):
            return True
        
        col_index = square%3
        column = [self.board[col_index+i*3] for i in range(3)]
        if all(s==letter for s in column):
            return True

        # Only check the diagonals if the input lies on the diagonal[0,2,4,6,8] 
        if square%2==0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all(s==letter for s in diagonal1):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all(s==letter for s in diagonal2):
                return True
        return False

    
def play_game(game,player_x,player_o,print_game=True):
    #return winner or none for tie
    if print_game:
        game.print_board_nums()
    
    #starting letter
    letter = 'X'
    
    #keep iterating(getting and making moves) while the game has empty squares
    while game.empty_squares():
        if letter=='X':
            square = player_x.get_move(game)
        else:
            square = player_o.get_move(game)
        #making a move
        # print(game.make_move(letter,square))
        if game.make_move(letter,square):
            if print_game:
                print(f"{letter} makes a move to square {square}")
                # see the new board
                game.print_board()
                print('')
            #check if there is a winner after every move
            if game.current_winner:
                print(f'{letter} wins!')
                return letter
            letter = 'X' if letter == 'O' else 'O'
            #tiny pause to make board more readable
            if print_game:
                time.sleep(1)
    if print_game:
        print("It's a tie!")

if __name__=='__main__':
    player_x = HumanPlayer('X')
    player_o = GeniusComputerPlayer('O')
    t = TicTacToe()
    play_game(t,player_x,player_o,print_game=True )



