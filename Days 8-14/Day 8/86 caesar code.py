alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text,shift,direction):
    direction = direction.lower()
    output_text = []
    encoded = ""
    if shift > 26:
        shift = shift % 26

    for i in text:
        if i in alphabet:
            old_index = alphabet.index(i)
            if direction == "encode":
                new_index = old_index + shift
                if new_index > 25:
                    new_index -= 26
            elif direction == "decode": 
                new_index = old_index - shift
                if new_index < 0:
                    new_index += 26
            encoded += alphabet[new_index]
        else:
            encoded += i
    print(encoded)


run_again = True
while run_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text = text, shift = shift, direction = direction)
    again = input("Do you want to run again?")
    again = again.lower()
    if again == "yes":
        run_again = True
    else:
        print("Bye")
        run_again = False

