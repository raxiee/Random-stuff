
def print_repeatedly(string):
    for i in range(10000):
        if i < 10:
            print(string + '000' + str(i))
        elif i < 100:
            print(string + '00' + str(i))
        elif i < 1000:
            print(string + '0' + str(i))
        else:
            print(string + str(i))

print_repeatedly('campusvejle')

import os


def save_combinations_to_file(string, filename):
    directory = r'C:\Users\64921\Documents\John the Ripper\run'
    filepath = os.path.join(directory, filename)

    with open(filepath, 'w') as file:
        for i in range(10000):
            if i < 10:
                file.write(string + '000' + str(i) + '\n')
            elif i < 100:
                file.write(string + '00' + str(i) + '\n')
            elif i < 1000:
                file.write(string + '0' + str(i) + '\n')
            else:
                file.write(string + str(i) + '\n')


save_combinations_to_file('campusvejle', 'wordlist.txt')
