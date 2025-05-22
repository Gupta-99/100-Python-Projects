import random
print("Welcome to Rock, Paper, Scissors!")
c=int(input("Type\n 1 for Rock\n 2 for Paper\n 3 for Scissors "))
if c==1:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif c==2:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    
elif c==3:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
else:
    print("Wrong Input")
    
print("Computer chose : ")
r=random.randint(1,3)
if r==1:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif r==2:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    
elif r==3:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    
if c==1 and r==1:
    print("DRAW")
elif c==1 and r==2:
    print("YOU LOST!")
elif c==1 and r==3:
    print("YOU WIN!")
elif c==2 and r==1:
    print("YOU WIN!")
elif c==2 and r==2:
    print("DRAW")  
elif c==2 and r==3:
    print("YOU LOST!")
elif c==3 and r==1:
    print("YOU LOST!")
elif c==3 and r==2:
    print("YOU WIN!")  
elif c==3 and r==3:
    print("DRAW")

