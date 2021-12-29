## HARRY POTTER AND THE FIRST YEAR ADVENTURE GAME ##
## This UserComm class will focus on communicating with the end user (i.e. player) of the game. 

# Import relevant py files
from card import Card

# Class: UserComm
class UserComm():
    ''' The UserComm class is the class used to help communicate with the player/user.'''
    
    def welcome():
        '''UserComm.welcome() prints the welcome messages at the beginning of the game.'''
        print("\n HARRY POTTER AND THE FIRST YEAR ADVENTURE GAME \n Welcome to Hogwarts young Witches and Wizards! Time for a little adventure game first years!  ")
        print("To win, you need to move past 10 spaces. \n You will draw a card on each space to help you move across the board. \n But first we need your name.")
    
    def player_profile(pname,phouse):
        '''UserComm.player_profile() prints the player's name and sorted Hogwarts House.'''
        print ((str(pname) + ', you have been sorted into ' + str(phouse) + '!'))
    
    def player_board_start():
        '''UserComm.player_board_start() helps the user know that introductions are done
        and the game will start.
        '''
        print("Now that your board has been set up, let's start playing!")

    def drawn_card_print(the_card):
        '''UserComm.drawn_card() will print the card that the person has drawn to move across the board.'''
        Card.card_print(the_card)

    def player_won(pname, phouse):
        '''UserComm.player_won() will show the user a message if they win the game.'''
        print((str(pname) + ' , CONGRATULATIONS! You have won the this game! You have made ' + str(phouse) + ' proud :)'))

    def player_lost(pname, phouse):
        '''UserComm.player_lost() will show the user a message if they lose the game.'''
        print (('I\'m sorry ' + str(pname) + ' , you are out of cards and out of luck. You have lost this game. ' + str(phouse) + ' house is sad :('))  

    def player_quit():
        '''UserComm.player_quit() will print a message Thanking the user for playing
        the game, and confirming that they have quit the
        ''' 
        print("You have quit the game. Thank You for taking the time to play.")   
        

