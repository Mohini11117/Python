import random
print("comp turn: snake('s') water('w') gun('g'): ")
you=input("your turn: snake('s') water('w') gun('g'): ")

def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=='g':
        if you=='w':
            return True
        elif you=='s':
            return False
    elif comp=='w':
        if you=='s':
            return True
        elif you=='g':
            return False
    elif comp=='s':
        if you=='w':
            return False
        if you=='g':
            return True
randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'

elif randNo==3:
    comp='g'
 
a=gamewin(comp,you)
print("computer choice is",comp)
print("your choice is",you)
if a==None:
    print("Its Tie!!!!")
elif a:
    print("Congrats!! you win!!")
else:
    print("Sorry!! you lose the game !")
 


      
