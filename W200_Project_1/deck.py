## HARRY POTTER AND THE FIRST YEAR ADVENTURE GAME ##
## This file will define the deck class and also run the 4 decks based on the different houses. 

# Import python packages
import random 

# Import from other py files
from card import Card

# Class: DeckClass 
class DeckClass():    
    '''The DeckClass class will manage the card decks used in 
    the game.
    '''
    def __init__(self, house_dict, house):
        '''Initialize DeckClass: there will be 4 decks/instances be based on the house,
        which in itself has different anecdote and value dictionary.
        '''
        self.house_dict = house_dict
        self.house = house
        self.deck_list = []
        self.build()
        
    def build(self):
        '''DeckClass.build will build the deck for one Hogwarts House.'''
        for key, value in self.house_dict.items():
            self.deck_list.append(Card(key, value, self.house))
        return (self.deck_list)

    def print_deck(self):
        '''DeckClass.print_deck will print the deck; 
        used more for development purposes.
        '''
        for cc in self.deck_list:
            Card.card_print(cc)
            
    def shuffle_deck(self):
        '''DeckClass.shuffle_deck will shuffle the deck in question.'''
        random.shuffle(self.deck_list)
    
    def draw_card(self):
        '''DeckClass.draw_card will draw 1 card which will be used to 
        help move the player on the board
        '''
        card_drawn = self.deck_list.pop()
        return (card_drawn)
    
    def len_deck(self):
        '''DeckClass.len_deck will get the number of cards remaining in the deck; 
        used more for development purposes.
        '''
        return len(self.deck_list)
    
    def deck_empty(self):
        '''DeckClass.deck_empty will find out if the deck is empty. This will be used to 
        inform whether the player has lost the game.
        '''
        if len(self.deck_list) == 0:
            return True
        else:
            return False 

    def __repr__(self):
        '''This DeckClass repr method prints out the deck list.'''
        return (self.deck_list)
        
            
