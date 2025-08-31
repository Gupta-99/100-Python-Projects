import random as rd

def deal_card():
    """Returns a random card from the deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = rd.choice(cards)
    return card

def calculate_score(cards):
    """Takes a list of cards and calculates the score of those cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "DRAW!!"
    elif c_score == 0:
        return "You LOSE! Opponent has BLACKJACK!"
    elif u_score == 0:
        return "You WIN! You have a BLACKJACK!"
    elif u_score > 21:
        return "You LOSE! You went over 21!"
    elif c_score > 21:
        return "You WIN! Opponent went over 21!" 
    elif u_score > c_score:
        return "You WIN!"
    else:
        return "You LOSE!"

def play_game():
    print("\nWELCOME TO BLACKJACK!\n")
    user_cards = []
    comp_cards = []
    user_score = -1
    comp_score = -1

    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())
            
    while not game_over:      
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)

        print(f"Your cards are : {user_cards}\nCurrent score : {user_score}")
        print(f"Computer's first card : {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
        else:
            user_deal = input("Type 'y' to deal card, Type 'n' to pass : ").lower()
            if user_deal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True
    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calculate_score(comp_cards)
        
    print(f"Your final hand : {user_cards}\nFinal score : {user_score}")
    print(f"Computer's final hand : {comp_cards}\nComputer's Final score : {comp_score}")
    print(compare(user_score, comp_score))
    
while input("Do you wanna play a game of BLACKJACK? Type 'yes' or 'no' : ").lower() == "yes":
    print("\n"*20)
    play_game()