## HARRY POTTER AND THE FIRST YEAR ADVENTURE GAME ##
## This file will run the player class

# Import python packages 
import random

# Class: players
class Player():
    '''The Player class is used to manage the attributes of the player/user.'''

    def __init__(self):
        '''Initialize Player: each player will have a defined
        name and Hogwarts House.
        '''
        # name
        self.name = input("Name:").title()
        # house
        hog_houses = ['Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin']
        self.house = random.choice(hog_houses) 
    
    def player_name(self):
        '''Function to return the player's name.'''
        return (self.name)
        
    def player_house(self):
        '''Function to return the player's name.'''
        return (self.house)
        
    def __repr__(self):
        '''Function to print class instance; more used in development.'''
        return((str(self.name) + ', you have been sorted into ' + str(self.house) + '!'))
