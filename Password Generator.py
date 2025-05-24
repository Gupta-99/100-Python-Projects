import random as rd
l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
n=['0','1','2','3','4','5','6','7','8','9']
sym=['!','@','#','$','%','&','*','(',')','+']

print("Welcome to your very own Password Generator!!")
no_of_letters=int(input("How many letters would you want in your password? : "))
no_of_numbers=int(input("How many numbers would you want in your password? : "))
no_of_symbols=int(input("How many symbols would you want in your password? : "))

Password=''

#Easy Lvl
for i in range(no_of_letters):
    Password+=rd.choice(l)
    
for i in range(no_of_numbers):
    Password+=rd.choice(n)

for i in range(no_of_symbols):
    Password+=rd.choice(sym)

print(f'Your Simpler Password is : {Password}')

#Hard Lvl
password=[]
for i in range(no_of_letters):
    password+=rd.choice(l)
    
for i in range(no_of_numbers):
    password+=rd.choice(n)

for i in range(no_of_symbols):
    password+=rd.choice(sym)
rd.shuffle(password)
PASSWORD=''
for i in password:
    PASSWORD+=i
print(f'Your Much Stronger password is : {PASSWORD}')