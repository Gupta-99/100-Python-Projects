print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island!!\n Your Mission is to find the TREASURE by making the right choices!!")
direction=input("You are at a crossroad! Where are you gonna go NEXT?! Type 'Left' or 'Right' ")
if direction == "left" or direction == "Left" or direction == "LEFT":
    swim=input("You have reached a River! What do you do NOW??!\n Type 'Swim' or 'Wait' ")
    if swim=="Swim" or swim=="swim" or swim=="SWIM":
        print("You were attacked by Trout!\n GAME OVER!")
    elif swim=="Wait" or swim=="wait" or swim=="WAIT":
        door=input("There are 3 Mysterious doors! Red, Blue, Yellow! Which one will you choose? ")
        if door=="Red" or door=="red" or door=="RED" or door=="R" or door=="r":
            print("Burned alive by Fire!!\n GAME OVER!")
        elif door=="Blue" or door=="blue" or door=="BLUE" or door=="B" or door=="b":
            print("The Beast devoured you!\n GAME OVER!")
        elif door=="Yellow" or door=="yellow" or door=="YELLOW" or door=="Y" or door=="y":
            print("You WIN!! YOU found the treasure!!")
        else:
            print("GAME OVER!")
else:
    print("You fell into a HOLE!\n GAME OVER!")            
        
            