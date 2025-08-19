print("Hello !\nWelcome to a Silent Auction !")


auction = {}

def auct(name,bid):
    auction[name] = bid
    


def highest_bid(bidding_dictionary):
    winner = ""
    highest_bid_amt = 0
    for bidder in bidding_dictionary:
        bid_amt = bidding_dictionary[bidder]
        if bid_amt > highest_bid_amt:
            highest_bid_amt = bid_amt
            winner = bidder
    print(f"The winning bidder is {winner} and the bid was : {highest_bid_amt} Rupees")
    
rerun = True

while rerun:

    your_name = input("Enter your name\n")
    your_bid = int(input("Place your bidding amount in Rupees\n"))
    
    auct(name = your_name, bid = your_bid)
    
    more_players = input("Are there any more bidders?\nType Yes or No\n").lower()
    
    if more_players == "no":
        rerun = False
        print(highest_bid(bidding_dictionary=auction))
    elif more_players == "yes":
        print("\n"*100)
    else:
        print("**************INPUT ERROR****************")  
    