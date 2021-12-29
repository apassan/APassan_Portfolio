## HARRY POTTER AND THE FIRST YEAR ADVENTURE GAME ##
## This file will help move the player across the board game. 

# Import python packages
import random 

#Import py files
from deck import DeckClass
from player import Player
from card import Card

# Class: HpBoard
class HpBoard(Player, DeckClass, Card):
    '''HpBoard class will help move the players at different
    points of the game until the end.'''
    
    def __init__(self):
        '''initalize HpBoard: The spaces and the board; used for development purposes.'''
        self.space_0 = 128
        self.space_1 = 134
        self.space_2 = 140
        self.space_3 = 146
        self.space_4 = 152
        self.space_5 = 158
        self.space_6 = 164
        self.space_7 = 170
        self.space_8 = 176
        self.space_9 = 182
        self.board = """
_____________________________________________________________
|     |     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |     |
|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|

"""

    def __repr__(self):
        '''This repr for HpBoard will print the board; more for development purposes.'''
        return print(self.board)
    
    def board_print(self):
        '''HpBoard.board_print will print the HpBoard instance.'''
        return print(str(self.board))

    def start_game(self):
        '''HpBoard.start_game will start the game by placing the player, 
        represented by an * in the first square.
        '''
        self.board = self.board[:self.space_0] + '*' + self.board[self.space_0 +1:]
        return print(self.board)     
        
    def start_turn(self, p_house, proper_deck):
        '''HpBoard.start_turn will first find the house of the player
        and call in the appropriate deck. Then the deck needs to
        be shuffled. Finally a card is drawn and printed to the user.
        '''
        # Need to get the house of the player 
        turn_house = p_house
        # Get the proper deck 
        proper_deck.shuffle_deck()
        # Draw card
        move_card = proper_deck.draw_card()
        return (move_card)
    
    def move_turn(self, card_value):
        '''HpBoard.move_turn will call the value from the drawn card 
        in the function above, multiply it by 6 to get the number
        of indexes we need to move the * in the board string to
        get the * in the right box.
        '''
        # Multiple value by 6
        in_to_change = card_value * 6
        # Find current index of *
        cur_in = self.board.find('*')
        # Replace the old * with blank 
        self.board = self.board[:cur_in] + ' ' + self.board[cur_in +1:]
        # Add in the * in the new spot 
        new_in = cur_in + in_to_change
        # Check if player can move forward
        if new_in > 182 or new_in < 128:
            self.board = self.board[:cur_in] + '*' + self.board[cur_in +1:]
            print("Sorry! There are not enough spaces left on the board to move. \n You will have to stay put for this turn.")
        else:
            self.board = self.board[:new_in] + '*' + self.board[new_in +1:]
        # Print the board
        return print(self.board)    
    
    def player_won(self):
        '''HpBoard.player_won checks whether a player has 
        reach the last place and won after their turn.
        '''
        return self.board[182] == '*'
    
    def player_lost(self, proper_deck):
        '''HpBoard.player_lost checks whether a player has
        run out of cards and thus lost after their turn.
        '''
        return proper_deck.deck_empty()