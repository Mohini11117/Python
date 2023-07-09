import math
import random
name=input("Enter Your name:")
print("Welcome to Tambola,",name,".")
n=int(input("How many players?"))
if(n<2 or n>10):
    print("wrong Input")
else:
    for i in range (0,n):
        print("player",i+1,":",end=' ')
        for j in range (0,9):
            print(random.choice(range(1,100)),end=' ')
        print()
print("Tambola;")
for i in range(0,n):
    for j in range(0,10):
        print(random.choice(range(1,100)),end='')
    print()
win=input("winner Name")
print("congrats,",win)

print("would you like to play again?",y/n)
if y:
    print("continue the game")
else:
    print("thanks for ")
