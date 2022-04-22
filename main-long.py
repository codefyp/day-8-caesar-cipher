#authors solution
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#direction = ("encode")
text = input("Type your message:\n").lower()
#text = ("civilization").lower()
shift = int(input("Type the shift number:\n"))
#shift = int(3)

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

#uses new functions as keyword arguments
def encrypt(plain_text, shift_amount):
    #creates an empty string to store the ciphered text
    cipher_text = ""
    #creates one loop to do all the ciphering
    for letter in plain_text:
        #creates a variable to hold each index position
        position = alphabet.index(letter)
        #creates a variable to hold the new shifted position
        new_position = position + shift_amount
        #converts it to a new letter by creating a new variable and finds each new letter by feching the position from the alphabet
        new_letter = alphabet[new_position]
        #now adds all the letters one by one to the cipher_text
        cipher_text += new_letter
    print (f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
    #creates an empty string to store the ciphered text
    decipher_text = ""
    #creates one loop to do all the ciphering
    for letter in cipher_text:
        #creates a variable to hold each index position
        position = alphabet.index(letter)
        #creates a variable to hold the new shifted position
        new_position = position - shift_amount
        #converts it to a new letter by creating a new variable and finds each new letter by feching the position from the alphabet
        new_letter = alphabet[new_position]
        #now adds all the letters one by one to the cipher_text
        decipher_text += new_letter
    print (f"The decoded text is {decipher_text}")    
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
    
    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

    ##solves the bug by copy and paste the entire alphabet 

    
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
    
#uses keyword argument to call the function

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)      
if direction == "decode":
    decrypt(plain_text=text, shift_amount=shift)
else:
    print("Oops, there is no such command")

