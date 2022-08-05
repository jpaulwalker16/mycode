#!/usr/bin/env python3

round = 0 #counter

while True:
    round = round + 1
    print('finish the movie title, "monty python\'s the life of ______"')
    answer = input(" your guess-->")

if answer == "shrubbery":
    print("you gave the super secret answer!")

#define variable as upper or lowercase
answer = answer.lower()

    if answer == 'Brian': #if statement
        print('correct')
        break

    elif round==3:
        print("sorry, the answer was Brian.")
        break

    else:
        print("sorry! try again!")



