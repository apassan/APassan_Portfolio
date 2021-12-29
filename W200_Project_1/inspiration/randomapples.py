options_dict = {'c1': 'card', 'c2':'card2, 'c3':'card3'}

user_pick = input("Which computer has the best card? You can only put in c1 c2 or c3").lower()


#double check if below is possible
while user_pick not in ['c1', 'c2', 'c3']:
    print('invalid input!')
    user_pick = input("Which computer has the best card? You can only put in c1 c2 or c3").lower()

# define your c score variables as 0 before the for loop in which you should some version of the below

def score(user_pick):
    if user_pick == 'c1':
        c1_score += 1
    elif user_pick == 'c2':
        c2_score += 1
    elif user_pick == 'c3':
        c3_score += 1
