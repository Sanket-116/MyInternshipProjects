#!/usr/bin/env python
# coding: utf-8

# In[35]:


import random

random_int = random.randint(1, 10)
count = 0

print("Guess the number between 1 to 10")
print("You get 4 guesses")

for x in range(1, 5):
    print("\nGuess no.", x)
    
    try:
        guess = int(input("Enter your guess: "))
        
        if 1 <= guess <= 10:
            if guess == random_int:
                print("Congratulations!! You guessed it right")
                count = 1
                break
            elif guess > random_int:
                print("You guessed a little high. Try again")
            else:
                print("You guessed a little low. Try again")
        else:
            print("Please enter a number between 1 to 10")
        
        print("No. of guesses left:", 5 - x)
    
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if count == 1:
    print("\nYou finished the game within", x, "tries!!🫡")
else:
    print("\nThank you for playing. Better luck next time!!🙂")


# In[ ]:





# In[ ]:




