## HARRY POTTER AND THE FIRST YEAR ADVENTURE GAME ##
## This file will run the player class. 

# class: card
class Card():
    '''The Card class will host the attributes of each
    individual card in the deck used.
    '''

    def __init__(self, anecdote, value, house):
        '''Initialize Card: each Card instance must have an anecdote that tells the player what happened,
        the value of the anecdote (i.e. how many spaces they must move back), and the 
        associated house it is in to know which deck the card is in.'''
        self.anecdote = anecdote
        self.value = value
        self.house = house
    
    def card_print(self):
        '''Function to print an individual card; used more for development purposes.'''    
        return (self.anecdote + '\n' + 'Move ' + str(self.value) +' spaces.')