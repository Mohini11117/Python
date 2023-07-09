import random
C=random.randint(1,100)
print(C)
userGuess=None
guess=0
while(userGuess!=C):
    userGuess=int(input("user Guess: "))
    if userGuess==C:
        print("Entered nuber is equgiven numberal to ")
    elif userGuess>C:
        print("Entered number is big")
    else:
        print("entered number is small")
