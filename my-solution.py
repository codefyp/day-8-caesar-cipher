alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
direction = ("encode")
#text = input("Type your message:\n").lower()
text = ("civilization").lower()
#shift = int(input("Type the shift number:\n"))
shift = int(3)

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text, shift):
    #create a text_list where we gonna save the letters from the imput word as seperate items
    text_list = list(text)
    #create an empty position_num list where we going to save the index numbers of each letter
    position_num = []
    #create a for loop to loop through our letter text_list and find which index number corresponds from the alphabet
    for letter in text_list:
        index = alphabet.index(letter)
        #then we add those numbers into our position_num list inside the loop
        position_num.append(index)
    #then we create a incremented_list where we add up the shift to our index numbers from position_num     
    incremented_list = [z+shift for z in position_num]
    #now we empty our text_list
    text_list = []
    #then we add into text_list the letters from the alphabet that corresponds into our added shift incremented_list
    text_list = [ alphabet[i] for i in incremented_list]
    #now we join all the letters together back to a single word from our text_list
    encrypt_text = "".join(text_list)
    print(encrypt_text)
if direction == "encode":
    encrypt(text, shift)      
else:
    print ("ha")
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
    
    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
