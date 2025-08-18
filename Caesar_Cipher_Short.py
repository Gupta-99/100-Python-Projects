L = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print("\nWELCOME TO YOUR CAESAR CIPHER!!\n")

def caesar(original_text,shift_no,choice):
    cipher_text = ""
            
    if choice == "decode":
        shift_no *= -1

    for letter in original_text:
        
        if letter not in L:
            cipher_text += letter
        else:
            new_pos = L.index(letter) + shift_no
            new_pos %= len(L)
            cipher_text += L[new_pos]
        
    print(f"Here is your {choice}d text : {cipher_text}")    

rerun = True
 
while rerun:
    text = input("Type your message : \n").lower()
    direction = input("Type 'Encode' for encryption and 'Decode' for decryption : \n").lower()
    shift = int(input("By how many letters do you wanna shift? : \n"))
    
    caesar(original_text=text,shift_no=shift,choice=direction)
    
    restart = input("Do you wish to re-run the program? Type yes or no : \n").lower()
    if restart == "no":
        rerun = False
        print("Goodbyee")