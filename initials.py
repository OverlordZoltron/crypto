def get_initials(fullname):
    #split the full name into chunks
    split_name = fullname.split()
    initials = ""
    #go through the split name
    for i in range(len(split_name)):
        #for every split select the first letter
        initials += split_name[i][0]
    #return the accumulated initials in uppercase
    return initials.upper()

#answer = get_initials("Daniel Day Lewis")
#print("The initials of 'Daniel Day Lewis' are", answer)

user_input = input("What is your name?")
print(get_initials(user_input))