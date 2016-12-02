def get_initials(fullname):
    split_name = fullname.split()
    initials = ""
    for i in range(len(split_name)):
        initials += split_name[i][0]
    return initials.upper()

answer = get_initials("Daniel Day Lewis")
print("The initials of 'Daniel Day Lewis' are", answer)