# Permutation will help in generating all the possible combinations of a given list of character

from itertools import permutations
from os import write
import string
import random

charset_list=['l', 'u', 'p', 'n', 'lu', 'ln', 'un', 'lp', 'up', 'np', 'lun', 'lup', 'unp', 'lunp']

# Defining these three as global varible so that it can be used easily in every function
charset=''
length=4
filename='vinay'

# Defining all the Charset using the String Module
l = string.ascii_lowercase
u = string.ascii_uppercase
p = string.punctuation
n = string.digits
lu = string.ascii_lowercase + string.ascii_uppercase
ln = string.ascii_lowercase + string.digits
un = string.ascii_uppercase + string.digits
lp = string.ascii_lowercase + string.punctuation
up = string.ascii_uppercase + string.punctuation
np = string.digits + string.punctuation
lun = string.ascii_lowercase + string.ascii_uppercase + string.digits
lup = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
unp = string.ascii_uppercase + string.digits + string.punctuation
lunp = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation


def generator(charset, length, filename):
    if charset == 'l':
        charset = l
    elif charset == 'u':
        charset = u
    elif charset == 'p':
        charset = p
    elif charset == 'n':
        charset = n
    elif charset == 'lu':
        charset = lu
    elif charset == 'ln':
        charset = ln
    elif charset == 'un':
        charset = un
    elif charset == 'lp':
        charset = lp
    elif charset == 'up':
        charset = up
    elif charset == 'np':
        charset = np
    elif charset == 'lun':
        charset = lun
    elif charset == 'lup':
        charset = lup
    elif charset == 'unp':
        charset = unp
    elif charset == 'lunp':
        charset = lunp

    # Generating word list
    charset=list(charset)
    word_list=permutations(charset, length)
    word_list=list(word_list)
    word_list=str(word_list)
    
    with open('filename.txt', 'w') as f:
        f.write(word_list)
    print("Thanks for using this Tool")    


# This is the main part of the program which will act as a interface for the User
def driver():
    try:
        charset = input("Select the Charset: ")
        if charset == 'help':
            with open("instruction.txt") as f:
                myfile=f.read()
                print(myfile)
            driver()

        elif charset == 'exit':
            print("Thanks for using this Tool")
            exit(0)

        elif charset not in charset_list:
            print("Please select a valid charset!!!")
            driver()
        
        length=int(input("Enter the Length of the Password: "))
        
        filename = input("Enter the Filename: ")
        # Filename can not start with a number, program will generate error while creating output file
        number_list = ['0','1','2','3','4','5','6','7','8','9']
        if filename.startswith(tuple(number_list)):
            print("Filename cannot Start with a Number")
            driver()

    except ValueError:
        print("Please select a valid Length of Password")
        driver()
    except:
        print("Entered an Invalid Option")

    # Calling the Generator Program to Generate the Word List
    generator(charset, length, filename)


# Executing the Main Function Here
if __name__=='__main__':
    driver()