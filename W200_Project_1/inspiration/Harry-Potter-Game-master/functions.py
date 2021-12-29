
# coding: utf-8

# In[1]:


#HP_game is the function that holds the entirety of the game
# This is the function cycles the user through while loops of different options and decisions
def HP_game():
    """Text-based game utilizing connected while loops as different scenarios
    
    Parameters
    ----------
    input : string
        If user-inputted string matches string in while loop, loop value will change
    
    Returns
    -------
    output : string
        The output string will contain part of a storyline or instructions for how the user should proceed
    """
    loop = 1
    print("___________________________________________________________________")
    print("Welcome to the Magical World of Witchcraft and Wizardry.")

    while True:
#Start the game
        while loop == 1:
            if loop == 1:
                print("___________________________________________________________________")
                print("Chapter 1: The Magic Begins")
                print("Happy birthday! Eleven years old? Wow! You're practically an adult now!")
                print("But wait? You've opened all your presents, what's this mysterious letter?")
                print("It's sealed with some fancy wax and a stamp. The writing is clearly addressed to you, written in green ink. But you dont recognize who sent it")
                letter = input("What do you want to do?")

            if letter.lower() == ("read envelope"):
                print("___________________________________________________________________")
                print("It's made out of some old parchment and bears your name in green ink. It's sealed shut with a wax stamp decorated with some weird crest")
            elif letter.lower() == ("open letter"):
                print("___________________________________________________________________")
                print("The letter reads:")
                print("HOGWARTS SCHOOL of WITCHCRAFT and WIZARDRY") 
                print("Headmaster: ALBUS DUMBLEDORE")      
                print("""(Order of Merlin, First Class, Grand Sorc., Chf. Warlock, Supreme Mugwump, International Confed. of Wizards)""")
                print("Dear Mr/Ms. YOURNAME")
                print("We are pleased to inform you that you have been accepted at Hogwarts School of Witchcraft and Wizardry.")
                print("Please find enclosed a list of all necessary books and equipment.")
                print("Term begins on 1 September. We await your owl by no later than 31 July.")
                print("     Yours sincerely,")
                print("     Minerva McGonagall")
                print("     Deputy Headmistress")
                print("")
                print("HOGWARTS SCHOOL of WITCHCRAFT and WIZARDRY")
                print("")
                print("UNIFORM")
                print("First-year students will require:")
                print("     1. Three sets of plain work robes (black)")
                print("     2. One plain pointed hat (black) for day wear")
                print("     3. One pair of protective gloves (dragon hide or similar)")
                print("     4. One winter cloak (black, with silver fastenings)")
                print("  Please note that all pupils’ clothes should carry name tags.")
                print("")
                print("COURSE BOOKS")
                print("  All students should have a copy of each of the following:")
                print("     1. The Standard Book of Spells (Grade 1) by Miranda Goshawk")
                print("     2. A History of Magic by Bathilda Bagshot")
                print("     3. Magical Theory by Adalbert Waffling")
                print("     4. A Beginner’s Guide to Transfiguration by Emeric Switch")
                print("     5. One Thousand Magical Herbs and Fungi by Phyllida Spore")
                print("     6. Magical Drafts and Potions by Arsenius Jigger")
                print("     7. Fantastic Beasts and Where to Find Them by Newt Scamander")
                print("     8. The Dark Forces: A Guide to Self-Protection by Quentin Trimble")
                print("")
                print("OTHER EQUIPMENT")
                print("     1. 1 wand")
                print("     2. 1 cauldron (pewter, standard size 2)")
                print("     3. 1 set glass or crystal phials")
                print("     4. 1 telescope")
                print("     5. 1 set brass scales")
                print("     6. Students may also bring an owl OR a cat OR a toad.")
                print("")
                print("PARENTS ARE REMINDED THAT FIRST YEARS ARE NOT ALLOWED THEIR OWN BROOMSTICKS.")
                loop = 2
            elif letter.lower() == ("throw away letter"):
                print("___________________________________________________________________")
                print("Why would you do that? Here, read it.")
            elif letter.lower() == ("tear letter in half"):
                print("___________________________________________________________________")
                print("Letter won't rip.")
            elif letter.lower() == ("burn letter"):
                print("___________________________________________________________________")
                print("The letter is somehow fireproof.")
            else:
                print("___________________________________________________________________")
                
    #enrollment
        while loop == 2:
            if loop == 2:
                print("___________________________________________________________________")
                print("Do you accept the invitation? ")
                enroll_inp = input("Yes or no?")

            if enroll_inp.lower() == ("yes"):
                print("___________________________________________________________________")
                print("The adventure begins!")
                loop = 3
            elif enroll_inp.lower() == ("no"):
                print("You've resigned yourself to life as a muggle")
                break
                
    #Diagon Alley
        while loop == 3:
            if loop == 3:
                print("___________________________________________________________________")
                print("Chapter 2: Diagon Alley")
                print("Now it's time to shop for supplies! The place to go for all your wizarding/witching needs is the imfamous Diagon Alley!.")
                print("Try to get everything on your list. When you're done, type 'end shopping trip'")
                diagon_alley = input("What do you want to buy? ")

            if diagon_alley.lower() == ("buy wand"):
                print("___________________________________________________________________")
                print("It's time to go to Ollivander's! The absolute best place for wands.")
                loop = 5
            elif diagon_alley.lower() == ("buy robes"):
                print("___________________________________________________________________")
                print("""We better be off to "Madam Malkin's Robes for All Occasions" then! The very best place for any wizarding-dress-ware! They have robes, dress robes, travelling cloaks, invisibilty cloaks, stop watches, regular watches, pants, shirts, anything you could ever need to wear!""")
                print("""Here you buy three sets of regular robes, a winter cloak, a pair of dragonhide gloves, and a pack of name tags. OH WE ALMOST FORGOT. You need a hat!""")
                print("Now you look the part of a wizard!")
            elif diagon_alley.lower() == ("buy cauldron"):
                print("___________________________________________________________________")
                print("Simple enough")
                print("All you need is one pewter cauldron. But, OH BOY that's quite heavy isnt it?")
            elif diagon_alley.lower() == ("buy pet"):
                print("The very best part of this trip! It's time to pick your very own animal companion!")
                loop = 4
            elif diagon_alley.lower() == ("end shopping trip"):
                print("You all ready to go? Alright! Lets go catch the train to Hogwarts!")
                loop = 7
            else:
                print("___________________________________________________________________")
                print("no action")
                print("hint: phrase it ""buy ___""")

    #Pet selection
        while loop == 4:
            if loop == 4:
                print("___________________________________________________________________")
                print("Welcome to the Diagon Alley petshop! There's a pet her for any young witch or wizard")
                print("Cages line the walls, each occupied by a different kind of pet.")
                print("You see cats, rabbits, toads, rats, and dozens upon dozens of owls")
                print(""""Hello!" the petshop owner greets you. "What kind of pet are you looking for today? Hogwarts student, right? Well that limits your choices to three. Would you like a cat, toad or owl?""")
                pet_selection = input("What kind of pet would you like? ")
            if pet_selection.lower() == ("cat"):
                print("___________________________________________________________________")
                print("'Perfect! I have just the thing for you! Here is an orange tabby, her name is 'Pumpkin Spice' after some Muggle invention. Give her a good home and take care of her and she will love you in return.'")
                print("")
                print("It's time now to do the rest of our shopping!")
                loop = 6
            elif pet_selection.lower() == ("toad"):
                print("___________________________________________________________________")
                print("""You are in luck!' I have just the specimen! Most people don't like toads as pets, but honestly they're one of the easiest to take care of--and between you an me, the easiest to transmute. They also don't shed like cats or tear up your carpets. This little guy's name is 'Tobby' but I bet he won't mind if you rename him.""")
                print("")
                print("It's time now to do the rest of our shopping!")
                loop = 6
            elif pet_selection.lower() == ("owl"):
                print("___________________________________________________________________")
                print("""You and everyone else! But fortunately I have a few available. This one's name is Volta and he's quite good at flying. Quite the escape artist as well--keep your eye on him! Once you get to school he can help you send letters and packages back to your folks.""")
                print("")
                print("It's time now to do the rest of our shopping!")
                loop = 6
            else:
                print("___________________________________________________________________")
                print("I don't think we have that. Pick something else")
                


    #Wand selection           
        while loop == 5:
            if loop == 5:
                print("The sign at the front of the store reads 'Ollivanders Makers of Fine Wands since 283 B.C.'")
                print("When you enter, a small bell chime rings in accordance to the movement of the door. Against the walls sit stacks up on stacks of wands as the entirety of the shop is filled with wands on bookshelves, aside for the desk that sits at the front of the store.")
                print("You walk up to the front and ring the bell")
                print("Soon after a man enters. After a brief discourse you find he is the owner of this shop, and has agreed to fit you for a wand")
                print("After a dozen odd measurements, he lays out three wands and asks you to pick one.")
                print("Theres's an long ebony one, a willowly elm one, and a short hazlewood wand")
                wand_select = input("Which wand do you pick to try? ")
            if wand_select.lower() == ("elm"):
                print("___________________________________________________________________")
                print("The long elm wand seems to call out to you, tempting you with ever glance at it.")
                print("You give into it, and reach to snatch it up. When you touch it, a mysterious warmth runs through your body.")
                print("Your hand glows and a familiar John Williams score can be heard from the back of the shop.")
                print("""'Perfect!' calls out the owner. 'The Wand Chooses the Wizard! And this one chooses you!'""")
                print("")
                print("It's time now to do the rest of our shopping!")
                loop = 6
            elif wand_select.lower() == ("hazlewood"):
                print("___________________________________________________________________")
                print("""As soon as you reach for the wand, sparks fly and a sonic boom materializes back towards the bookcases.""")
                print(" 'NOPE' yells the owner as he plucks the wand from your fingers.'Pick a different one'")
            elif wand_select.lower() == ("ebony"):
                print("___________________________________________________________________")
                print("You hear a small ringing coming from the black ebony wand.")
                print("You reach for it, and as you make contact, the ringing fills the room.")
                print("Perfect! yells the owner as he gives you the wand. 'Remember, the wand chooses the Wizard! ")
                print("It's time now to do the rest of our shopping!")
                loop = 6
            else:
                print('"please do not do that in the shop"')
    #Back to diagon alley   
        while loop == 6:
            if loop == 6:
                print("___________________________________________________________________")
                print("We're back in Diagon Alley!")
                print("Try to get everything else on your list. When you're done, type 'end shopping trip'")
                diagon_alley = input("What do you want to buy? ")

            if diagon_alley.lower() == ("buy wand"):
                print("___________________________________________________________________")
                print("It's time to go to Ollivander's! The absolute best place for wands.")
                loop = 5
            elif diagon_alley.lower() == ("buy robes"):
                print("___________________________________________________________________")
                print("""We better be off to "Madam Malkin's Robes for All Occasions" then! The very best place for any wizarding-dress-ware! They have robes, dress robes, travelling cloaks, invisibilty cloaks, stop watches, regular watches, pants, shirts, anything you could ever need to wear!""")
                print("""Here you buy three sets of regular robes, a winter cloak, a pair of dragonhide gloves, and a pack of name tags. OH WE ALMOST FORGOT. You need a hat!""")
                print("Now you look the part of a wizard!")
            elif diagon_alley.lower() == ("buy cauldron"):
                print("___________________________________________________________________")
                print("Simple enough")
                print("All you need is one pewter cauldron. But, OH BOY that's quite heavy isnt it?")
            elif diagon_alley.lower() == ("buy pet"):
                print("The very best part of this trip! It's time to pick your very own animal companion!")
                loop = 4
            elif diagon_alley.lower() == ("end shopping trip"):
                print("You all ready to go? Alright! Lets go catch the train to Hogwarts!")
                loop = 7
            else:
                print("___________________________________________________________________")
                print("no action")
                print("hint: phrase it ""buy ___""")
    #Platform 9 3/4           
        while loop == 7:
            if loop == 7:
                print("___________________________________________________________________")
                print("School supplies bought, luggage all packed, wand in hand--you're ready to go to Hogwarts!")
                print("But first, where do you go to get on your train? You see platform 9 and platform 10. But your train ticket clearly says Platform 9 3/4")
                platform934 = input("What do you do?")
                      
            if platform934.lower() == ("look around"):
                print("___________________________________________________________________")
                print("Just as you had begun to give up, you see a couple teenagers walk right through the barrier between platforms 9 and 10!")
            elif platform934.lower() == ("walk through barrier"):
                print("___________________________________________________________________")
                print("You've made it! Platform 9 3/4 is hidden from muggles and can be accessed by walking through the barrier between platforms 9 and 10")
                loop = 8
            elif platform934.lower() == ("ask for help"):
                print("___________________________________________________________________")
                print("You ask someone in very non-muggle clothes to assist you in finding the right platform. They instruct you to walk right through the barrier between the platforms")
                print("Following her lead you do just that, and stumble into a hidden platform")
                loop = 8
            
            else:
                print("___________________________________________________________________")
                print("Didnt work, try something else. Maybe walk somewhere or ask for help?")
                
    #Train
        while loop == 8:
            if loop == 8:
                print("___________________________________________________________________")
                print("Chapter 3: The Hogwarts Express")
                print("You've made it onto the Hogwarts express")
                print("There are two compartments with seats left, one on the right side, one on the left")
                hog_exp = input("Where do you sit? (left/right)")
                      
            if hog_exp.lower() == ("left"):
                print("___________________________________________________________________")
                print("You choose to sit in the left compartment at the far end of the train")
                print("Inside sit two girls who introduce themselves as Sarah and Rachel")
                print("Sarah was a ray of sunshine personified with bright green eyes and long blonde hair framing her grinning face.")
                print("In opposition, Rachel was quiet and brooding, with short brown hair just long enough to reach her chin.")
                print("Both were equally friendly, eager as you to get to the school")
                loop = 9
            elif hog_exp.lower() == ("right"):
                print("___________________________________________________________________")
                print("You choose to sit in the right compartment at the front of the train.")
                print("Inside sit a group of first-years. Two boys and one girl all about your age.")
                print("One of the boys and girl were twins, named Jason and Emma. They both had matching blue eyes and tawney hair.")
                print("The other boy's name is Carlos. His curly brown hair frames his face as he grins a gap-toothed smile.")
                print("You join in their excited conversation about what awaits you tonight at the school.")
                loop = 10

    #Entrance to Hogwarts 1
        while loop == 9:
            if loop == 9:
                print("___________________________________________________________________")
                print("After a long journey, your train has finally reached its destination.")
                print("An announcement comes over the loudspeaker, telling you all to get dressed in your school uniforms and ready")
                ent1 = input("Are you ready to enter Hogwarts? ")
        
            if ent1.lower() == ("yes"):
                loop = 11
            else: 
                print("well, you can stay on the train until you feel ready enough")
                      
    #Entrance to Hogwarts 2
        while loop == 10:
            if loop == 10:
                print("___________________________________________________________________")
                print("After a long journey, your train has finally reached its destination.")
                print("An announcement comes over the loudspeaker, telling you all to get dressed in your school uniforms and ready")
                ent2 = input("Are you ready to enter Hogwarts? ")
        
            if ent2.lower() == ("yes"):
                loop = 12
            else: 
                print("well, you can stay on the train until you feel ready enough")
    #Sorting 1
        while loop == 11:
            if loop == 11:
                print("___________________________________________________________________")
                print("You're led across the lake to the school on lantern-lit boats.")
                print("When you reach the school, you and the rest of the first years are ushered into the entrance hall.")
                print("Here you wait to be brought into the great feast.")
                print("Sarah seems nervous, her smile being replaced by anxiety. Rachel looked similar, twiling and untwirling her hair constantly.")
                print("Soon you all are ushered in for the sorting ceremony.")
                print("It's explained to all of you that a hat will be placed on your head and it will choose your house for you.")
                print("Sarah goes before you, stepping up to the front of the room")
                print("'HUFFLEPUFF' the hat calls out for all to hear")
                print("You then hear your name, calling you to the front of the room.")
                hall1 = input("Do you go up? (yes/no)")
                      
            if hall1.lower() == ("yes"):
                loop = 13
            else: 
                print("come on, you can do it!")
    #Sorting 2
        while loop == 12:
            if loop == 12:
                print("___________________________________________________________________")
                print("You're led across the lake to the school on lantern-lit boats.")
                print("When you reach the school, you and the rest of the first years are ushered into the entrance hall.")
                print("Here you wait to be brought into the great feast.")
                print("Your new friend group all seem nervous, gossiping among each other about what house they think they'll get.")
                print("Soon you all are ushered in for the sorting ceremony.")
                print("It's explained to all of you that a hat will be placed on your head and it will choose your house for you.")
                print("First are the twins, one after another")
                print("'SLYTHERIN' the hat announces for both of them.")
                print("Carlos goes up afterwards, quickly sorted into Ravenclaw.")
                print("You then hear your name, calling you to the front of the room to be sorted.")
                hall2 = input("Do you go up? (yes/no)")
                      
            if hall2.lower() == ("yes"):
                loop = 13
            else: 
                print("come on, you can do it!")
            

                      
    #Personal Sorting  
        while loop == 13:
            if loop == 13:
                print("___________________________________________________________________")
                print("Chapter 4: Your Sorting")
                print("You're really nervous as you step up to the front of the room.")
                print("Professor McGonagall places a ratty old hat on top of your head and waits for an answer.")
                print("'Such brains we have here! Such spirit!' whispers a voice in your head.")
                print("'Do you belong in Gryffindor, where your skills will reside in honor and loyalty?'")
                print("'Or maybe you'll put that big brain to use in Ravenclaw.'")
                print("'Perhaps it's Hufflepuff you're meant for, or maybe you're destined for greatness in Slytherin.'")
                print("'However, the choice is up to you'")
                sorting_hat = input("Which house do you pick?")
                      
            if sorting_hat.lower() == ("gryffindor"):
                loop = 14
            elif sorting_hat.lower() == ("ravenclaw"):
                loop = 15
            elif sorting_hat.lower() == ("slytherin"):
                loop = 16
            elif sorting_hat.lower() == ("hufflepuff"):
                loop = 17
            else: 
                print("No, try again!")
                
    #Gryff
        while loop == 14:
            if loop == 14:
                print("___________________________________________________________________")
                print("'GRYFFINDOR!' calls out the hat.")
                print("Congrats! Now go join your friends and you can look forward to a year of adventures before you!")
                  
                gryff_1 = input("Continue? (yes/no)") 
            if gryff_1.lower() == ("yes"):
                loop = 20
            else:
                print("lets wait here until you change your mind")
                      
    #Hufflepuff
        while loop == 15:
            if loop == 15:
                print("___________________________________________________________________")
                print("'HUFFLEPUFF!' calls out the hat.")
                print("Congrats! Now go join your friends and you can look forward to a year of adventures before you!")
                      
                huff_1 = input("Continue? (yes/no)") 
            if huff_1.lower() == ("yes"):
                loop = 20         
            else:
                print("lets wait here until you change your mind")

    #Ravenclaw
        while loop == 16:
            if loop == 16:
                print("___________________________________________________________________")
                print("'RAVENCLAW!' calls out the hat.")
                print("Congrats! Now go join your friends and you can look forward to a year of adventures before you!")
            
                raven_1 = input("Continue? (yes/no)") 
            if raven_1.lower() == ("yes"):
                loop = 20
            else:
                print("lets wait here until you change your mind")
                      
    #Slytherin
        while loop == 17:
            if loop == 17:
                print("___________________________________________________________________")
                print("'SLYTHERIN!' calls out the hat.")
                print("Congrats! Now go join your friends and you can look forward to a year of adventures before you!")
                sly_1 = input("Continue? (yes/no)") 
            if sly_1.lower() == ("yes"):
                print("")
                loop = 20
            else:
                print("lets wait here until you change your mind")

    #End
        while loop == 20:
            if loop == 20:
                print("___________________________________________________________________")
                print("It looks like your story is done for now")
                end_inp = input("Do you wish to leave?")
    # Exit loop at the end of game
            exit_inp = input("Do you want to quit or restart the game? (quit/restart) ")
            if exit_inp.lower() == ("quit"):
                break
            if exit_inp.lower() == ("restart"):
                print("time turner in process")
                loop = 1
        return 


def HP_start():
    if True:
        print("Welcome to the Magical World of Witchcraft and Wizardry")
        print("Input your answer into the box below to start the game!")
        print("If you get stuck, see if the response is giving you a hint. If you still can't figure it out, look into the function code file to find an acceptable answer to input")
    return




