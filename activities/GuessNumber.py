# ---------------------------------

# File          : GuessNumber.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 30/09/2021
# Modified Date : 
# Description   : A sample program to guess a number between 1 to 20
# Licensing     : Anup Jacob, LYIT
# ----------------------------------


# print("Enter any number between 1 to 20")

y = int(input("Do you wish to play the game : (0/1) : "))

while y != 0:

    x = int(input("Enter any number between 1 to 20 : "))

    NumValue = 15

    if (x == 15) :
        print("Your guess was correct!. Congratulations")
    elif (x > 20):
        print("The number you have chosen is beyond the limit specified.")
    elif (x < 1):
        print("The number you have chosen is below the limit specified.")
    else:
        print("Your guess was wrong!. Please try again.")

    y = input("Do you wish to play again: (0/1) : ")



print(y)



print("\n"+"Thank you for playing the Guessing game")
