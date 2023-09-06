#Guess number Game

import random

print("This is a Game, You Have to Guess a Number Between a Range.")
i = "Y"

while i == "Y":
    a1, a2 = input("\n Enter two value As Range(Seperated by Space): ").split()
    rnd = random.randint( int(a1) , int(a2) )
    attempt = 1
    while True :
        y = int(input("Enter your Guess: "))
        if rnd == y:
            print (":) :) You Are Amazing :) :) The number Was ",y)
            print ("You achieved to the right answer by", attempt, "times guesses.")
            i = input("\n Do you Want to Reapeat the Game? (Y/N): ")
            break
        elif rnd < y:
            print("Wrong:(  Enter Lesser Number \n")
            attempt+=1
        else:
            print("Wrong:(  Enter Higher Number \n")
            attempt+=1
