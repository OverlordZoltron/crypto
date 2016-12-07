def alphabet_position(letter):
    if (ord(letter) >= 97) and (ord(letter) <= 122):
        return ord(letter)-97
    elif (ord(letter) >= 65) and (ord(letter) <= 90):
        return ord(letter)-65
    else:
        pass


def rotate_character(char, rot):
    #check if lowercase
    if (ord(char) >= 97) and (ord(char) <= 122):
        return chr(97+(alphabet_position(char)+rot)%26)
    #check if uppercase
    elif (ord(char) >= 65) and (ord(char) <= 90):
        return chr(65+(alphabet_position(char)+rot)%26)
    #if neither, return the character
    else:
        return char

def encrypt(text, rot):
    new_text = ""
    for char in range(len(text)):
        new_text += rotate_character(text[char],int(rot))
    return new_text

print(encrypt(input("A message to cypher"),input("Rotate by:")))