#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time

def introduction():
    print("Welcome to 'Quest for the Lost City'!\n")
    time.sleep(2)
    print("You are an adventurous archaeologist who has discovered an ancient map hinting at the existence of a lost city deep within an uncharted jungle.\n")
    time.sleep(2)
    print("Your journey begins...\n")
    time.sleep(2)
    start_game()

def start_game():
    print("You find yourself at the edge of the jungle. You have a backpack with some supplies.")
    while True:
        choice = input("What will you do? (Enter 'explore' to venture into the jungle or 'quit' to exit the game): ").lower()
        if choice == 'explore':
            explore_jungle()
        elif choice == 'quit':
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Please enter a valid choice.")

def explore_jungle():
    print("\nYou begin your journey into the dense jungle...")
    time.sleep(2)
    print("You encounter a river. You need to cross it.")
    choice = input("Will you 'swim' across the river or 'build a raft'? ").lower()
    if choice == 'swim':
        print("You decide to swim. It's a risky move, but you make it to the other side.")
    elif choice == 'build a raft':
        print("You gather materials and build a raft to cross the river safely.")
    else:
        print("Please enter a valid choice.")

    # Continue the game with more interactions, puzzles, and choices.

if __name__ == '__main__':
    introduction()


# In[8]:


import time

class NinjaCharacter:
    def __init__(self, name):
        self.name = name
        
        self.missions = {"1":"1. Find the Queens lost cat (parsi).","2":"2. Escort a convoy of marchant to the nighorbing country"}


def introduction():
    print("Welcome to 'Shinobi's Path: Journey with Your Sensei'!")
    time.sleep(2)
    print("You are a young ninja-in-training in the hidden village of Konohagakure.")
    time.sleep(2)
    print("You have been assigned a legendary sensei who will guide you on your path to becoming a powerful shinobi.")
    time.sleep(2)
    print("Your journey begins...\n")
    time.sleep(2)

    name = input("Enter your character's name: ")
    player = NinjaCharacter(name)
    
    print(f"\nWelcome, {player.name}! Your sensei, Kakashi sensie, is waiting for you.")
    time.sleep(2)

    start_game(player)

def start_game(player):
    while True:
        print("\nYou find yourself in Konohagakure, ready to begin your training as a shinobi.")
        time.sleep(2)
        print("Your sensei, Kakashi of the sharingan is standing by. Your missions and adventures await.")
        time.sleep(2)
        
        choice = input("What will you do? (Enter 'missions' to check your missions or 'quit' to exit the game): ").lower()
        if choice == 'missions':
            missions_list(player)
        elif choice == 'quit':
            print("\nThanks for playing! Goodbye.")
            break
        else:
            print("Please enter a valid choice.")

def missions_list(player):
    if not player.missions:
        print("\nYou don't have any missions yet. Wait for your sensei's instructions.")
    else:
        print("\nYour current missions:")
        for mission in player.missions:
            print("- " + mission)
    time.sleep(2)
    
    
def mission_selection():
    mission_no=input("Select the mission by Entering it's sr.no")
            if mission_no == 

if __name__ == '__main__':
    introduction()


# In[10]:


import time

class NinjaCharacter:
    def __init__(self, name):
        self.name = name
        self.missions = {"1": "Find the Queen's lost cat (parsi).", "2": "Escort a convoy of merchants to the neighboring country"}

def introduction():
    print("Welcome to 'Shinobi's Path: Journey with Your Sensei'!")
    time.sleep(2)
    print("You are a young ninja-in-training in the hidden village of Konohagakure.")
    time.sleep(2)
    print("You have been assigned a legendary sensei who will guide you on your path to becoming a powerful shinobi.")
    time.sleep(2)
    print("Your journey begins...\n")
    time.sleep(2)

    name = input("Enter your character's name: ")
    player = NinjaCharacter(name)
    
    print(f"\nWelcome, {player.name}! Your sensei, Kakashi of the Sharingan, is waiting for you.")
    time.sleep(2)

    start_game(player)

def start_game(player):
    while True:
        print("\nYou find yourself in Konohagakure, ready to begin your training as a shinobi.")
        time.sleep(2)
        print("Your sensei, Kakashi of the Sharingan, is standing by. Your missions and adventures await.")
        time.sleep(2)
        
        choice = input("What will you do? (Enter 'missions' to check your missions or 'quit' to exit the game): ").lower()
        if choice == 'missions':
            missions_list(player)
        elif choice == 'quit':
            print("\nThanks for playing! Goodbye.")
            break
        else:
            print("Please enter a valid choice.")

def missions_list(player):
    if not player.missions:
        print("\nYou don't have any missions yet. Wait for your sensei's instructions.")
    else:
        print("\nYour current missions:")
        for mission_num, mission_desc in player.missions.items():
            print(f"{mission_num}. {mission_desc}")
        mission_selection(player)

def mission_selection(player):
    while True:
        mission_no = input("Select a mission by entering its serial number, or enter 'back' to return to the previous menu: ")
        if mission_no in player.missions:
            selected_mission = player.missions[mission_no]
            print(f"You have chosen to undertake the mission: {selected_mission}")
            time.sleep(2)
            

            if mission_no == 1:
                cat()
            else:
                escort()
                
        elif mission_no.lower() == 'back':
            break
        else:
            print("Please enter a valid mission number.")

def cat():
    print("Be very worrior this mission is of atmost importance as the cat we have find in close to Queen!!!")
    time.sleep(2)
    print("\\   For finding the cat you have recived a generous reward from the queen and a word of thanks.     // ")
    

def escort():
    print("The marchats are carring valuable so they might get attcaked by bandits be on gaurd always.")
    time.sleep(2)
    print("\\   Phew, That was exusting be but you made it without a scratch, Now have a breather NINJA!   //")
    
    
    
if __name__ == '__main__':
    introduction()


# In[ ]:


import time



def epilog():
    print("Welcome to 'Ninja Word with Kakashi Sensei'")
    time.sleep(2)
    print("You are a young ninja-in-training in the hidden village of leafs.\n")
    time.sleep(2)
    print("You have been assigned a legendary sensei who will guide you on your path to becoming a powerful shinobi.")
    time.sleep(2)
    print("Your journey begins...\n")
    time.sleep(2)

    player = input("Enter your character's name: ")


    print(f"\nWelcome, {player}! Your sensei, Kakashi of the Sharingan, is waiting for you.")
    time.sleep(2)

    start_game(player)

def start_game(player):
    while True:
        print("\nReady to begin your training ninja.")
        time.sleep(2)
        print("Your sensei, Kakashi of the Sharingan, waiting. Your missions and adventures await.")
        time.sleep(2)

        choice = input("What will you do? (Enter 'mission' to check your missions or 'quit' to exit the game): ").lower()
        if choice == 'mission' or 'missions':
            missions_list(player)
        elif choice == 'quit':
            print("\nThanks for playing! Goodbye.")
            break
        else:
            print("Please enter a valid choice.")

def missions_list(player):
    print("\nYour current missions:")
    print("1. Find the Queen's lost cat (Parsi).")
    print("2. Escort a convoy of merchants to the neighboring country.")
    mission_selection(player)

def mission_selection(player):
    while True:
        mission_choice = input("Select a mission by typing keyword, or type 'back' to return to the previous menu:  \n'cat' for 1st mission \n'escort' for 2nd mission \n\n").lower()
        if mission_choice == 'cat':
            cat(player)
        elif mission_choice == 'escort':
            escort(player)
        elif mission_choice == 'back':
            break
        else:
            print("Please enter a valid keyword ('cat', 'escort') or 'back'.")

def cat(player):
    
    print("Be very cautious! This mission is of utmost importance as the cat is close to the Queen!")
    print("...")
    time.sleep(4)
    print("For finding the cat, you have received a generous reward from the Queen and her thanks.\n\n")
    print("Congartulation on compleeting your mission {player}")
def escort(player):
    print("The merchants are carrying valuable goods and might be attacked by bandits. Stay on guard at all times.")
    print("...")
    time.sleep(4)
    print("Phew, that was exhausting, but you made it without a scratch. Now, have a breather, NINJA!\n")

if __name__ == '__main__':
    epilog()


# In[ ]:




