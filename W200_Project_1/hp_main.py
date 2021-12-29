## HARRY POTTER AND THE FIRST YEAR ADVENTURE GAME ##
## This is the main file needed to run the game

# import packages
import random

# import py files
from player import Player
from card import Card
from deck import DeckClass
from hp_board import HpBoard
from user_comm import UserComm

# Plan of attack for running the game:
'''
1. Run the welcome message.
2. Enter the player name
3. Assign the player's house
4. Show the player their name and house profile
5. Get their deck ready 
6. Start the game by printing the board with the '*' in the first square
7. Take a turn  
    a. START the turn by shuffling the deck, drawing a card, and printing said drawn card
    b. MOVE the player by accessing the value of the card, multiply it by 6, and either 
       add or subtract that number from the current '*' index to move the player on the
       board string. If the final index is greater than [182], then the player doesn't move.
    c. END the turn by first checking whether the player's index is at board[182] to see
       if they won; next if they have not won, check if the deck length is 0 to see if they
       have lost the game. 
8. If they have won, show the won message; if they have lost, show
   the you have lost message. 
'''

# Relevant house dictionaries that will be imported to the main() function if the relevent house gets chosen.
# Gryffindor House Dictionary
g_dict = {'Professor Snape caught you smuggling sweets from the kitchens. You have detention cleaning Mrs. Norris\' litterbox.': -1, 
          'Congratulations! You made the Gryffindor quidditch team as a first year. Get ready to catch that Golden Snitch Seeker!': 2, 
          'Oops! You fell asleep in History of Magic during one of Professor Binn\'s lectures on Goblin wars. You have detention cleaning out bedpans in the hospital without magic.': -1, 
          'You just had your first potions exam and you passed! Good job!': 1, 
          'You successfully transfigured a mouse into a snuffbox WITHOUT whiskers. Great job!': 2, 
          'You won 100 galleons in a karoke contest with your fellow first years. Congratulations!': 1, 
          'You just had the best treacle tart in your life at the Christmas feast. Boy are you a happy camper.': 3, 
          'You helped Professor Sprout clean up after herbology class out of the goodness of your heart. 1 point to Gryffindor!': 1, 
          'You won the annual Gryiffindor pie eating contest by eating 5 pumpkin pies in 4 minutes. Now go rest your stomach.': 2, 
          'Your customized Gryffindor lion belt finally arrived. The rubies on the belt really bring out the sparkle in your eyes.': 1}

# Ravenclaw House Dictionary
r_dict = {'Professor Snape caught you smuggling sweets from the kitchens. You have detention cleaning Mrs. Norris\' litterbox.': -1, 
          'Congratulations! You made the Ravenclaw quidditch team as a first year. Get ready to score some goals as Chaser!': 2, 
          'Oops! You fell asleep in History of Magic during one of Professor Binn\'s lectures on Goblin wars. You have detention cleaning out bedpans in the hospital without magic.': -1, 
          'You just had your first potions exam and you passed! Good job!': 1, 
          'You successfully transfigured a mouse into a snuffbox WITHOUT whiskers. Great job!': 2, 
          'You won 100 galleons in a karoke contest with your fellow first years. Congratulations!': 1, 
          'You just had the best treacle tart in your life at the Christmas feast. Boy are you a happy camper.': 3, 
          'You helped Professor Sprout clean up after herbology class out of the goodness of your heart. 1 point to Ravenclaw!': 1, 
          'You got the highest grade on the Defense Against the Dark Arts exam of all the first years. Well done!': 2, 
          'Your customized Ravenclaw sweater came in the mail today. Not only does it look good on you, but it\'s super soft too!': 1}

# Hufflepuff House Dictionary
h_dict = {'Professor Snape caught you smuggling sweets from the kitchens. You have detention cleaning Mrs. Norris\' litterbox.': -1, 
          'Congratulations! You made the Hufflepuff quidditch team as a first year. Get ready to defend some goals as Keeper!': 2, 
          'Oops! You fell asleep in History of Magic during one of Professor Binn\'s lectures on Goblin wars. You have detention cleaning out bedpans in the hospital without magic.': -1, 
          'You just had your first potions exam and you passed! Good job!': 1, 
          'You successfully transfigured a mouse into a snuffbox WITHOUT whiskers. Great job!': 2, 
          'You won 100 galleons in a karoke contest with your fellow first years. Congratulations!': 1, 
          'You just had the best treacle tart in your life at the Christmas feast. Boy are you a happy camper.': 3, 
          'You helped Professor Sprout clean up after herbology class out of the goodness of your heart. 1 point to Hufflepuff!': 1,  
          'You won the annual Hufflepuff house Gobstones tournament. Congratulations!': 2, 
          'Your customized black and yellow Hufflepuff Witch/Wizards hat came in the mail. It is confirmed, your head looks great in a hat.': 1}

# Slytherin House Dictionary
s_dict = {'Professor Snape caught you smuggling sweets from the kitchens. But you\'re a Slytherin so he doesn\'t care.': 1, 
          'Congratulations! You made the Slytherin quidditch team as a first year. Get ready to wack some bludgers as Beater!': 2, 
          'Oops! You fell asleep in History of Magic during one of Professor Binn\'s lectures on Goblin wars. You have detention cleaning out bedpans in the hospital without magic.': -1, 
          'You just had your first potions exam and you passed! Good job!': 1, 
          'You successfully transfigured a mouse into a snuffbox WITHOUT whiskers. Great job!': 2, 
          'You won 100 galleons in a karoke contest with your fellow first years. Congratulations!': 1, 
          'You just had the best treacle tart in your life at the Christmas feast. Boy are you a happy camper.': 3, 
          'You helped Professor Sprout clean up after herbology class out of the goodness of your heart. 1 point to Slytherin!': 1, 
          'Your customized Slytherin scarf with your name embroidered in silver thread just came through, and it looks very dashing.': 2, 
          'You got lost getting back to the common room in the dungeons again.': -1}


# main() function to run the game
def main():
    '''This main() function for Harry Potter and the First Year Adventure Game will call the 5 classes
    (Player, Card, DeckClass, HpBoard, and UserComm) to interact with each other to run the game.'''
    # Print the Welcome messages and get the player's name and Hogwards House set up
    UserComm.welcome()
    print('\n')
    our_player = Player()
    # Print the user profile
    UserComm.player_profile(pname = Player.player_name(our_player), phouse = Player.player_house(our_player))
    # Get the corresponding Hogwarts house deck made as part of the game set up
    if Player.player_house(our_player) == 'Gryffindor':
        game_deck = DeckClass(house_dict = g_dict, house = Player.player_house(our_player))
    elif Player.player_house(our_player) == 'Ravenclaw':
        game_deck = DeckClass(house_dict = r_dict, house = Player.player_house(our_player))
    elif Player.player_house(our_player) == 'Hufflepuff':
        game_deck = DeckClass(house_dict = h_dict, house = Player.player_house(our_player))
    elif Player.player_house(our_player) == 'Slytherin': 
        game_deck = DeckClass(house_dict = s_dict, house = Player.player_house(our_player))
    # 10-space square board set up 
    board_set = HpBoard()
    board_set.start_game()
    # Inform the player/user that the game is now ready to play
    UserComm.player_board_start()
    print('\n')
    # A turn is run until the player either wins, loses, or chooses to quit to end the game
    while True:
        user_continue = input('Please press any letter(s), number(s), or character(s) or the enter key to start your turn and continue the game. If you would like to quit the game, you may press the single letter q or Q.')
        if user_continue == 'q'or user_continue == 'Q':
           UserComm.player_quit()
           break
        chosen_card = board_set.start_turn(p_house = Player.player_house(our_player), proper_deck = game_deck)
        print('\n')
        print(chosen_card.anecdote + '\n' + 'Move ' + str(chosen_card.value) +' space(s).')
        print('\n')
        board_set.move_turn(chosen_card.value)        
        if board_set.player_won() == True:
            UserComm.player_won(pname = Player.player_name(our_player), phouse = Player.player_house(our_player))
            break
        elif board_set.player_lost(game_deck) == True:
            UserComm.player_lost(pname = Player.player_name(our_player), phouse = Player.player_house(our_player))
            break


# To play Harry Potter and the First Years Adventure Game, run main()
main()