def alphabet_position(letter):
    if (ord(letter) >= 97) and (ord(letter) <= 122):
        return ord(letter)-97
    elif (ord(letter) >= 65) and (ord(letter) <= 90):
        return ord(letter)-65
    else:
        pass