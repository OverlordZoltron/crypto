from sys import argv, exit
from helpers import rotate_character


def encrypt(text, rot):
    #create new string
    new_text = ""
    #for each char in the text
    for char in range(len(text)):
        #rotate that character according to the ROT and put it in the new string
        new_text += rotate_character(text[char], int(rot))
    return new_text


def user_input_is_valid(cl_args):
    if len(cl_args) == 1:
        return False
    elif cl_args[1].isdigit():
        return True
    else:
        return False


def main():
    if len(argv) == 1:
        print("usage: python3 " + argv[0] + " n")
        exit()
    if user_input_is_valid(argv):
        message = input("Type a message:\n")
        print(encrypt(message, int(argv[1])))
    else:
        print("usage: python3 " + argv[0] + " " + argv[1])
        exit()


if __name__ == '__main__':
    main()
