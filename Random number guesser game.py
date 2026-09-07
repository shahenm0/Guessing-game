import random

playagain = "yes"

while playagain.lower() == "yes":
    randomnumber = random.randint (0, 10)
    userguess = int(input("Guess random number between 0-10:"))

    while userguess != randomnumber:
        userguess = int(input ("Wrong! Try again:"))
    print ("Well done! you guess right!")
    playagain = input ("Want to play again?")

print("Thanks for playing!")
