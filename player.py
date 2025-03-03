import math
import random

class Player:
    def __init__(self,letter):
        # letter is x or o
        self.letter = letter
    
    #not sure what this does rn
    def get_move(self,game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)
    
    def get_move(self,game):
        #make computer make a random move from the list of available moves
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        #let human choose a move from the list of available moves
        valid_square = False
        val = None
        while not valid_square:
            square = input(f"{self.letter}'s turn. Choose an input between 0-8: ")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid Square. Please try again')
        return val
class GeniusComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)
    
    def get_move(self,game):
        if len(game.available_moves())==9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game,self.letter)['position']
        return square
    
    def minimax(self,state,player):
        # choose the most optimal path by taking the max value computed for our turn and min val 
        # computed for the other player's turn
        max_player = self.letter
        prev_player = 'O' if player == 'X' else 'X'

        #check if the previous move is a winner
        if state.current_winner is not None:
            if state.current_winner == max_player:
                return {'position': None, 'score': 1 * (state.num_empty_squares() + 1)}
            else:
                return {'position': None, 'score': -1 * (state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}
        
        #set best for max_player(us) and the other player
        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        
        for possible_move in state.available_moves():
            #make a move
            state.make_move(player,possible_move)
            # simulate a game after making that move
            sim_score = self.minimax(state,prev_player)
            #undo a move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best

