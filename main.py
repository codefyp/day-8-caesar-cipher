#authors solution mjqqt
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#uses new functions as keyword arguments
def caesar(start_text, shift_amount, cipher_direction):
    #creates an empty string to store the ciphered text
    end_text = ""
    #if statement to check if its decode and do a negative sum plus the shift_amount
    if cipher_direction == "decode":    
        shift_amount *= -1
    #creates one loop to do all the ciphering
    for char in start_text:
        if char in alphabet:
            #creates a variable to hold each index position
            position = alphabet.index(char)
            #creates a variable to hold the new shifted position
            new_position = position + shift_amount   
            #converts it to a new char by creating a new variable and finds each new char by feching the position from the alphabet
            end_text += alphabet[new_position]
        else:
            end_text += char
    print (f"The {cipher_direction} text is {end_text}")
#create the loop to keep the script running
should_end = False
while not should_end:
    #import the logo    
    from art import logo
    print(logo)
    #inputs
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    #make the shift to work with any high number by dividing the total number of the alphabet
    shift = shift % 26
    #trigger our function
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    #asks if you want to keep the script running
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
