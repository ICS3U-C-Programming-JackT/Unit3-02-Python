#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: March 15th, 2025

# Number guessing program in python


def main():

    # Define the program number, ask user for a number between 1 and 5
    programNumber = 1
    userNumber = int(input("Enter a number between 1 and 5:  "))
    correct = False
    if userNumber == programNumber:
        correct=True
        print("YOU GUESSED RIGHT!!! 🥳")

    # Check if number is higher or lower than the program number
    if (userNumber > programNumber or userNumber < programNumber):
        print("Aww, not the right answer, sorry!")

    # Check if number is within the range
    if userNumber > 5 or userNumber < 1:
        print("Please enter a number within the proper range (1-5)")
        
    if (correct==False):
        main()  # Fire main function to restart   


if __name__ == "__main__":
    main()  # Fire main function to begin
