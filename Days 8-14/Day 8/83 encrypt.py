alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

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

def encrypt(text,shift):
    output_text = []
    list_text = list(text)
    for i in list_text:
        old_index = alphabet.index(i)
        new_index = old_index + shift
        if new_index > 25:
            new_index -= 26
        output_text += alphabet[new_index]

    encoded = ""
    for l in output_text:
        encoded += l
    print(encoded)

def decrypt(text,shift):
    output_text = []
    list_text = list(text)
    for i in list_text:
        old_index = alphabet.index(i)
        new_index = old_index - shift
        if new_index < 0:
            new_index += 26
        output_text += alphabet[new_index]

    decoded = ""
    for l in output_text:
        decoded += l
    print(decoded)

direction = direction.lower()
if direction == "encode":
    encrypt(text = text, shift = shift)
elif direction == "decode":
    decrypt(text = text, shift = shift)
else:
    print("wrong parameter for direction")

