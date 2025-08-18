import random as rd
import Hangman_resources as hr
word_choice = rd.choice(hr.words)

print(hr.logo)

placeholder = ""
correct_letters = []
lives = 6

for i in range(len(word_choice)):
    placeholder +="_"

print(placeholder)

game_over = False
while not game_over:
    print(f"**********************{lives}/6 LIVES LEFT************************")
    
    user_choice = input("Guess a letter : ").lower()
    
    if user_choice in correct_letters:
        print(f"You have already guessed the letter {user_choice}")
    
    display = ""
    for ltr in word_choice:
        if ltr == user_choice:
            display += ltr
            correct_letters.append(ltr)
        elif ltr in correct_letters:
            display += ltr
        else:
            display += "_"
            
    print(display)
    
    if "_" not in display:
        game_over = True
        print("*****************************You Win!**************************")
    
    if user_choice not in word_choice:
        lives -= 1
        print(f"You guessed {user_choice}, it is not in the Word. You Lose a life.")
        if lives == 0:
            game_over = True
            print(f"*************************IT WAS {word_choice}! You Lose!*************************")
            
    print(hr.stages[lives])
    
    





