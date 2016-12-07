from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    #create new string
    new_text = ""
    #for each char in the text
    for char in range(len(text)):
        #rotate that character according to the ROT and put it in the new string
        new_text += rotate_character(text[char], int(rot))
    return new_text

def main():
    message = input("Type a message:\n")
    # 'The crow flies at midnight!
    rotate = input("Rotate by:")
    # boom
    print(encrypt(message, rotate))


if __name__ == '__main__':
    main()