#SEMESTER PROJECT PART B
#A text-based adventure game.
#By Janell Brown.  Completed April 29, 2022.
#Based on the code of the text adventure game found here: https://www.thecoderpedia.com/blog/text-based-adventure-game-in-python/

#For my video, I'll quickly run through the game and get two different endings to show that it works.

#My Changes:
"""
I changed the story.  Mine is longer with more endings and way more print functions (so many print functions).  
However, I kept the if elif format of the original.

I added a health system.  It consists of the health variable and is changed with the check_health function.
I use the game_over function to end the game when health drops below 0, or when an ending is reached.    

I added an inventory system.  It starts with the inventory list.  At the beginning of the game items are added
to that list with the add_item function (mainly in the throne room section), depending on user input.  
I use if elif statements to do different things based on what is in the inventory.

I improved the flow of the game.  Instead of ending the game if the user answers something other than yes/no,
I keep prompting the user for a yes/no with the check_answer function.  I also make it easy for the user
to restart the game after they reach the end.  I do this by surrounding the game in a while loop,
with an 'end' variable to help control the loop and a game_over function.

"""


#Starting variables.
answer_yes = ["Yes", "Y", "yes", "y", "YES", "YEs", "yES", "yEs", "YeS"]
answer_no = ["No", "N", "no", "n", "NO", "nO",]
health = 10
inventory = ["Dungeon Key"]
end = "repeat"

#Some functions to make game management easier.

def check_answer(ans): #There are a lot of yes/no questions so this will check for yes/no answers.

    while ans not in answer_yes and ans not in answer_no:
        if ans not in answer_yes and ans not in answer_no:
            ans = input("Type yes or no\n>>  ")
    return ans

def game_over(end = end): #A function to end the game.
    print("Press enter to continue.")
    wait = input(">>  ")
    print("\nGAME OVER.  Type 'repeat' to try again.  Type anything else to exit.")
    end = input(">> ")
    if end.lower() == "repeat":
        
        print("-----------Going Again!-----------")
        
    else:
        exit()
    return end

def add_item(item, list): #A function for whenever a new item is added.
   
    if item != "Empty":
        if len(list) >= 3:
            print(f"\nTo make room for it, you dropped the {list[0]}.")
            list.remove(list[0])
        list.append(item)
        
        print("\nYou now have the following items: ")
        for object in list:
            print(f"""     {object}""")
    else:#I use the empty item to reset the inventory for each round.
        list = ["Dungeon Key"]
        return list
   
    return list

def change_health(increase, amount, health): #This function will increase or decrease health.
    if (increase):
        health = health + amount
        print("\nYou gained health and now have", health, "HP.")
        print("Press enter to continue")#Wait for the player's input after health changes.
        wait = input(">>  ")
    
    else:
        health = health - amount
        print("\nYou lost health and now have", health, "HP.") #Wait for input after health changes.
        print("Press enter to continue")
        wait = input(">>  ")
        if health <= 0:
            print("Your injuries are too much for you to take.  YOU DIED.")
    return health


while end.lower() == "repeat":
    #MAKING SURE VALUES ARE WHAT THEY SHOULD BE IF THE GAME RESTARTS.
    end = "repeat"
    inventory = add_item("Empty", inventory)
    health = 10
   
    #THIS IS ADVENTURE'S INTRO.
    print("""
    You aren't a bad person.  It was all a misundertanding, in my opinion.  But the fact
    remains that you tried to steal from a 1,000 year old zombie king's castle and that made him sad.
    Zombie kings have feelings too, you know. 

    REMEMBER:
    There are 9 endings.  
    You have a backpack that stores items based on count instead of size or weight.  You can
    store three items at a time.  If you try to pick up another item when your backpack is full the oldest item
    will be dropped.

    ALSO:  The game is over when you make a really bad choice and have no health left.  You start with 10 HP.

    Press enter to continue.
    """)

    wait = input(">>  ")#These wait for the user to press enter.

    #FIRST CHOICE.
    print("\nTo earn the zombie king's forgiveness, you agreed to stay in his prison.")
    print("You only agreed after he locked you in, but you did agree nonetheless.")  
    print("Thankfully, you have the key to get out.")

    print("\nWould you like to leave?")

    print("\n(Yes / No)")


    ans1 = input(">>  ")

    ans1 = check_answer(ans1)

    if ans1 in answer_yes:        #PLAYER CHOOSES TO LEAVE

        print("\nYou open the door easily.")  
        print("From there you and your backpack travel down the cobblestone hallway.")
        print("There are many other cells, but they're all empty except for a pile of bones in the final cell.")  
        
        #SEEING THE RING
        print("\nYou look closer, and see a golden ring on the floor, just inches away from boney fingers.")  
        print("Aside from the Dungeon Key your backpack is empty.")
        print("This is a chance to add another item to your collection.")
        
        print("\nWould you like to take the ring?")
        
        
        
        #CHOICE TO GRAB THE RING
        print("\nYes / No")
        ans2 = input(">>  ")
        
        ans2 = check_answer(ans2)

        if ans2 in answer_yes: #SECOND CHOICE 'YES' PATH GRABBING RING
           
            inventory = add_item("Golden Ring", inventory)
    
            print("\nGood thing the dungeon key works for every cell.")  
            print("You open the barred door, grab the ring, and add it to your backpack.")
            print("You don't know if it's your conscience or something else, but you feel a little weird.")
            health = change_health(False, 4, health)
            print("You exit the hallway feeling a little dizzy.")
            
        elif ans2 in answer_no: #SECOND CHOICE 'NO' PATH LEAVING RING
            print("\nWho knows where that's been?")
            print("Leaving the ring behind, you exit the hallway.")
        
        
        print("\nPress enter to continue.")
        wait = input(">> ")
        
        #Entering the throne room.--------------------------
        print("\nYou climb up a staircase which leads to a heavy door.")
        print("Upon opening the door, a grand room covered in gold and red is before you.")
        print("There are two thrones to your left.  Both are about the size of small houses.")
        print("Various paintings cover the wall, too big to steal.")
        print("The only other noteworthy objects are three chests surrounding the thrones.")
        print("There's one between you and the first throne, one in front of the two thrones, and another to the right of the second throne.")
        print("Given your position and the size of the two thrones, you shouldn't really be able to see the last two chests, but you know about them anyway.")
        print("Oh, there's also a horse-sized dog in front of the second chest.")
        print("It snores.")
        
        #THIRD CHOICE--LOOTING CHESTS
        print("\nWould you like to loot any of the chests?  If not you'll leave the room.")
        print("\n(Yes/No)")

        ans3 = input(">>  ")
        
        ans3 = check_answer(ans3)

        if ans3 in answer_yes: #THIRD CHOICE 'YES' PATH. LOOTING
            #CHEST NUMBER 1-CHOICE TO LOOT
            print("\nThe first chest is the closest to you. Loot it?")
            print("\n(Yes/No)")

            loot = input(">>  ")

            loot = check_answer(loot)

            if loot in answer_yes:
                print("\nIt's a book.  A large book.  You take it.")
                inventory = add_item("Large Book", inventory)
            elif loot in answer_no:
                print("\nYou're right, you're too good for that one.")
           
           
            print("\nThe next chest is in front of the throne, but the dog is right in front of it.  Loot it?")
             #CHEST NUMBER 2-CHOICE TO LOOT
            print("\n(Yes/No)")
            
            loot = input(">>  ")

            loot = check_answer(loot)
           
            if loot in answer_yes:#IF PLAYERS LOOTS
                print("\nYou carefully creep towards the chest.")
                print("You can clearly see the dog's chest rising and falling.")
                print("His snores continue.")
                print("You sneak behind the dog and peer inside the chest.  There's a sword.")
                inventory = add_item("Beautiful Sword", inventory)
                print("The dog suddenly jerks awake.")
                print("With your new sword, you kill him with a few slashes, but not before he takes a bite out of your arm.")
                health = change_health(False, 4, health)
                print("\nWith the dog dead, the third chest is ready for the taking.  You want it?")

            elif loot in answer_no:#IF PLAYER DOES NOT LOOT
                print("\nIt's too risky, isn't it?")
               
                print("\nWhat about the third chest?")
                print("It's on the other side of the throne and would require you to walk in front of the dog.")
            
            #CHEST NUMBER 3- CHOICE TO LOOT
            print("\n(Yes/No)")
            loot = input(">>  ")

            loot = check_answer(loot)
            
    
            if loot in answer_yes:#IF PLAYER CHOOSES TO LOOT
                print("\nYou reach the chest with no issue.")
                print("Inside there's a Rubik's Cube.")
                print("Do you still wanna take it?  I mean, it seems kind of worthless...")
                
                print("\n(Yes/No)")
                loot = input(">>  ")
                loot = check_answer(loot)

                if loot in answer_yes:#IF PLAYER REAFFIRMS DECISION TO LOOT
                    inventory = add_item("Rubik's Cube", inventory)

            print("\nAnd so you move on to the next room, stepping through the giant throne room doors.")
          
            
        elif ans3 in answer_no: #THIRD CHOICE 'NO' PATH.
            print("Oh, you're no fun.  But you move on to the next room, stepping through the massive throne doors.")
        
        #Entering the courtyard.--------------
        print("\nYou uneventfully creep through the castle until you make your way through the courtyard and--what do you know?")
        print("A massive battle is taking place between modern man and zombie knights.  How did you not hear them?")
        print("Oh well.  This is the last obstacle standing between you and well-deserved freedom.")
        
        #CHOICE TO GO THROUGH COURTYARD
        print("\nWould you like to go straight through the crowd?  If not you'll go around.")
        print("\n(Yes/No)")
        
        ans4 = input(">>  ")
        ans4 = check_answer(ans4)

        if ans4 in answer_yes:#GOING THROUGH PATH
            print(f"\nWith a deep breath, you plunge into the battlefield.")
            print("There's a mixture of people and zombies on every side of you.")
            print("The clang of swords makes your ears ring.  The gunfire is deafening.")
            print("A zombie crashing into you suddenly causes you to collapse.")
            print("You fall and he falls on top of you.")
            
            #AN ENEMY APPEARS.
           
            if "Beautiful Sword" in inventory:#Fend him of with the sword
                print("You grab/summon your sword from your backpack and stab it, sustaining just a scratch.")
                health = change_health(False, 1, health)
                if health <= 0:
                    game_over()
                    continue

           
            elif "Large Book" in inventory:#Fend him off with the book
                print("\nYou grab/summon the book.")
                print("Your plan is to beat the zombie over the head with it, but it flips open and there's a flash of light.")
                print("When it clears, the zombie is gone.")
                print("However, in the time it took for you to open the book you took some damage.")
                health = change_health(False, 3, health)
                if health <= 0:
                    game_over()
                    continue

            elif "Rubik's Cube" in inventory:#fend him off with the cube.

                print("\nDo you know how to solve a Rubik's Cube by any chance? Be honest >:(")
                rubikAns = input(">>  ")
                rubikAns = check_answer(rubikAns)
                
                if rubikAns in answer_yes:
                    print("\nIt's the best you have, so you pull out the Rubik's Cube.")
                    print("The zombie was about to bite your neck, but he stops.  He's curious.")
                    print("He lets you sit up and solve the Rubik's Cube.  He even claps when you're done.")
                    print("He claps in a zombified kind of way.")
                    print("You stare at each other awkwardly, before you continue on you way.")
                    print("Solving the Rubik's Cube made you feel healthier.")
                    health = change_health(True, 3, health)
                    if health <= 0:
                        game_over()
                        continue
                    
               
                elif rubikAns in answer_no:
                    print("\nWell, it's the best you have, so you pull out the Rubik's Cube.")
                    print("The zombie was about to bite your neck, but he stops and stares.")
                    print("He wants to see you solve the Rubik's Cube, but you don't know how.")
                    print("He gets angry and bites your hand, but he also seems disappointed.")
                    health = change_health(False, 7, health) 
                    if health <= 0:
                        game_over()
                        continue
                    print("His eyes start to swell with tears.  Instead of doing any more harm to you, he runs away.")
                    print("He's crying in a zombie kind of way.")
                   


            else:
                print("\nThe only worthwhile thing you have is the Dungeon Key.")
                print("By using brute force and by poking the zombie with the key repeatedly, you mange to make him leave.")
                print("However he damages you quite a bit.")
                health = change_health(False, 8, health)
                if health <= 0:
                        game_over()
                        continue
                    
            #THE ENDING
            print("\nYou encounter more zombies, but you manage to make it around them unscathed.")
            print("You reach the castle gates.")
            print("Oh no!  The drawbrdige is gone!")
            
            print("With no other choice, you jump into the river and attempt to swim across.")
            if health <= 2:#If you're health is too low you'll get a different ending.
                print("\nHowever, you're injuries mean you aren't strong enough to make it.")
                print("RIP.")
                print("RIVER ENDING")
                game_over()
            else:
                print("\nIt's an exhausting task.")
                print("You barely make it to the other side, but you do.")
                print("You drag yourself onto the river bank, catch your breath, and head home.")
                print("SWAM FREE ENDING")
                game_over()

        elif ans4 in answer_no:#TO GO AROUND
            print("\nI suggest going left.  If you select 'no' you'll go right.")
            
            #CHOICE TO GO LEFT OR RIGHT.
            print("\n(Yes/No)")
            ans5 = input(">>  ")
            ans5 = check_answer(ans5)
            
            if ans5 in answer_yes:#GOING LEFT PATH
                print("\nWith a deep breath, you begin making your way around the courtyard.")
                print("You go left, going around and outside of the chaos.")
                print("The sound of gunshots and clashing swords makes for an awful combination.")
                print("Thankfully for you, however, the eventful thing that happens isn't so eventful.")
                print("There's a man in your path.  He's sitting at a desk.")
                
                #CHOICE TO TALK TO THE MAN
                print("Would you like to stop and talk to him?")
               
                print("\n(Yes/No)")
                ansTalk = input(">>  ")
                ansTalk = check_answer(ansTalk)
                
                if ansTalk in answer_yes:#TALKING TO THE MAN
                    print("You say 'hello' and sit down at the table.")
                    print("'Oh, hello fellow.'")
                    
                    if "Golden Ring" in inventory: #If player has the ring
                        print("'You seem to have a cursed object on you.'")
                        print("'I like cursed things.  Give it to me, and in exchange I'll take you from this wretched place.'")
                        #A CHOICE TO GIVE THE MAN THE RING.
                        print("\nGive him the ring?")
                        print("\n(Yes/No)")

                        ansRing = input(">>  ")
                        ansRing = check_answer(ansRing)

                        if ansRing in answer_yes: #GIVING MAN THE RING
                            print("\nYou give the man the ring.")
                            print("He smiles and with a snap of his fingers, everything goes black.")
                            print("When you wake up, it's like your standing on a cloud.")
                            print("There are kittens and puppies and a mansion made of diamonds a few ways away.")
                            print("It seems like you'll never see your friends or family again, but depending on your priorities this is a good ending.")
                            print("MANSION ENDING")
                            game_over()
                        else: #REFUSING TO GIVE HIM THE RING
                            print("\n'Rather selfish, don't you think?'") 
                            print("'Maybe you deserve something different'")
                            print("He smiles and with a snap of his fingers, everything goes black.")
                            print("When you wake up, your back in the dungeon cell.")
                            print("But this isn't the cell you were originally in.  This is where you found the ring!")
                            print("Even worse your backpack is gone!")
                            print("And with your backpack gone, and the dungeon key missing, you have no way out.")
                            print("Only this time you have a prison mate: a skeleton whose ring you stole.")
                            print("TRAPPED ENDING")
                            game_over()
                    else: #ALT CONVERSATION WITH MAN
                        print("\n'You don't seem like you're meant to be in this war.'")
                        print("'Let me do you a favor and take you away from this'")
                        print("The man smiles, and with a snap of his fingers, everything goes black.")
                        print("When you wake up, you're outside the castle walls, on the other side of the moat, perfectly in tact.")
                        print("The sun is bright, the hills are alive, the birds are singing.")
                        print("With nothing stopping you, you break into a sprint towards home.")
                        print("FREEDOM ENDING")
                        game_over()
               
                elif ansTalk in answer_no: #NOT TALKING TO THE MAN
                    print("Wish I could tell you how, but you died.")
                    print("??? ENDING")
                    game_over()
            
            if ans5 in answer_no:#GOING RIGHT PATH
                print("\nWith a deep breath, you begin making your way around the courtyard.")
                print("You go right, going around and outside of the chaos.  Most of it.")
                print("Only one thing gets in your way, and that thing is a zombie dragon.")
                
                if "Rubik's Cube" in inventory: #IF PLAYER HAS Rubik's CUBE.
                    print("\nI'm sorry to say it, but there's nothing you can do against a dragon.")
                    if "Beautiful Sword" in inventory:
                        print("Even the sword you have is no good, despite what legends would have you believe.")
                    print("You take out your Rubik's Cube, prepared to say goodbye to it.")  
                    print("You've grown quite attached to it.")
                    print("For some reason this scares the dragon and he flies away as quickly as he came.")
                    print("You're able to walk out the castle gates.")
                    print("SCARE DRAGON ENDING")
                    game_over()
                else:

                    print("\nI'm sorry to say it, but there's nothing you can do against a dragon.")
                    print("Not with an inventory like yours anyway.")
                    if "Beautiful Sword" in inventory:
                        print("Even the sword you have is no good, despite what legends would have you believe.")
                    print("A blast of fire flows from the dragon's mouth, engulfing you in heat.")
                    health = change_health(False, 9.5, health)
                    if health <= 0:
                        game_over()
                        continue
                    else:
                        print("Wow, you survived?")
                        print("I mean, you survived.")
                        print("Well then let's say...")
                        print("..A friendlier dragon arrives, pities you, and carries you away from the castle of horrors.")
                        print("ADOPTED BY DRAGON ENDING")
                        game_over()
                    
                       





    elif ans1 in answer_no:     #CHOOSING TO STAY IN CELL
        print("\nWhen you make a decision you don't back down.  As a result, you stay there until the end of time.")
        print("EARLY ENDING")
        game_over()
           

    else: #If player somehow manages to avoid choosing yes or no.
        game_over()
        