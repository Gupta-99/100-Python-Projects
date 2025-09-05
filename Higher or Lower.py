from HLgame_data import data
import random as rd

print(r"""
 __   __  ___   _______  __   __  _______  ______      _______  ______   
|  | |  ||   | |       ||  | |  ||       ||    _ |    |       ||    _ |  
|  |_|  ||   | |    ___||  |_|  ||    ___||   | ||    |   _   ||   | ||  
|       ||   | |   | __ |       ||   |___ |   |_||_   |  | |  ||   |_||_ 
|       ||   | |   ||  ||       ||    ___||    __  |  |  |_|  ||    __  |
|   _   ||   | |   |_| ||   _   ||   |___ |   |  | |  |       ||   |  | |
|__| |__||___| |_______||__| |__||_______||___|  |_|  |_______||___|  |_|
 ___      _______  _     _  _______  ______                              
|   |    |       || | _ | ||       ||    _ |                             
|   |    |   _   || || || ||    ___||   | ||                             
|   |    |  | |  ||       ||   |___ |   |_||_                            
|   |___ |  |_|  ||       ||    ___||    __  |                           
|       ||       ||   _   ||   |___ |   |  | |                           
|_______||_______||__| |__||_______||___|  |_|                                                  
      """)

print("\nGuess who has more followers!\n")

index1 = rd.randint(0,len(data)-1)
index2 = rd.randint(0,len(data)-1)
score = 0

def play_game():
    chosen_name_a = data[index1]["name"]
    chosen_profession_a = data[index1]["description"]
    chosen_location_a = data[index1]["country"]

    chosen_name_b = data[index2]["name"]
    chosen_profession_b = data[index2]["description"]
    chosen_location_b = data[index2]["country"]

    if data[index1]["follower_count"] > data[index2]["follower_count"]:
        win = "a"
    elif data[index1]["follower_count"] <= data[index2]["follower_count"]:
        win = "b"

    print(f"Current Score : {score}")
    print(f"A : {chosen_name_a}, {chosen_profession_a}, from {chosen_location_a}.")
    print(f"B : {chosen_name_b}, {chosen_profession_b}, from {chosen_location_b}.")


game_over = False

while not game_over:
    if data[index1]["follower_count"] > data[index2]["follower_count"]:
        win = "a"
    elif data[index1]["follower_count"] <= data[index2]["follower_count"]:
        win = "b"
    play_game()
    user_guess = input("Make your guess, A or B : ").lower()
    if user_guess == win:
        score += 1
        index1,index2 = index2,rd.randint(0,len(data)-1)
        
    else:
        game_over = True
        print(f"You LOST!\nScore = {score}")