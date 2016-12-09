import itertools
from helpers import alphabet_position, rotate_character


def encrypt(message, key):
    idx = 0
    cipher = []

    x = itertools.cycle(key)

    key_str = "".join(next(x) if c.isalpha() else c for c in message)

    while idx < len(message):
        cipher.append(rotate_character(message[idx], alphabet_position(key_str[idx])))
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