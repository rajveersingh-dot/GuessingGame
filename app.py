#   File:       app.py
#   Project:    guess
#   Date:       20/7/2022
#   Author:     Rajveer Singh <20069870@tafe.wa.edu.au>
#   Purpose:    (description)

import random


def main():
    num = random.randint(0, 100)
    num_of_tries = 0
    while True:
        data = input("Enter a number between the range of 0 - 100: ")
        data = int(data)
        if data < num:
            print('higher')
        if data > num:
            print('lower')
        if data == num:
            print('Correct ' + str(num_of_tries))
        elif data != num:
            num_of_tries += 1


if __name__ == '__main__':
    main()
