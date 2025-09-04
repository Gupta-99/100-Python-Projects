import random as rd

print(r"""
  ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/       
      """)
print("I will guess a number from 1 to 100, you need to guess the number!")
chosen_num = rd.randint(1,100)

difficulty = input("Choose a difficulty : 'Easy' or 'Hard'\n").lower()
if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5
print(f"You have {lives} lives left.")
game_over = False

def checker():
    global guess
    global lives
    global game_over
    
    if guess > chosen_num:
        lives -= 1
        print(f"Too High! You have {lives} lives left.")
    if guess < chosen_num:
        lives -= 1
        print(f"Too Low! You have {lives} lives left.")
    if guess == chosen_num:
        print(f"You Got It! The answer was indeed {chosen_num}")
        game_over = True
        

while not game_over:
    guess = int(input("Guess The Number : "))
    checker()
    if lives == 0:
        print(f"You LOSE! The answer was {chosen_num}")
        game_over = True
        
     

