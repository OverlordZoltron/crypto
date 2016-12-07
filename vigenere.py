def alphabet_position(letter):
    # check if lowercase
    if (ord(letter) >= 97) and (ord(letter) <= 122):
        return ord(letter)-97
    # check if uppercase
    elif (ord(letter) >= 65) and (ord(letter) <= 90):
        return ord(letter)-65
    # if neither, pass over this step
    else:
        pass


def rotate_character(char, rot):
    r = alphabet_position(rot)
    #check if lowercase
    if (ord(char) >= 97) and (ord(char) <= 122):
        return chr(97+(alphabet_position(char)+r)%26)
    #check if uppercase
    elif (ord(char) >= 65) and (ord(char) <= 90):
        return chr(65+(alphabet_position(char)+r)%26)
    #if neither, return the character
    else:
        return char


def encrypt(message, key):
    idx = 0
    cipher = []
    while idx < len(message):
        cipher.append(rotate_character(message[idx], key[idx % len(key)]))
        idx += 1
    return ''.join(cipher)


def main():
    message = input("Message:\n")
    # 'The crow flies at midnight!
    rotate = input("Encryption key:\n")
    # boom
    print(encrypt(message, rotate))


if __name__ == '__main__':
    main()