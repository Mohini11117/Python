class calculater:
    #num=int(input("Please Enter a Number"))
    #square=num*num
    #=num
    def __init__(self,num):
        self.number=int(input("enter a num : "))
    def square(self):
        print("The square of a given number is",self.number**2)
        print("***************************************************")
    def cube(self):
        print("The cube of a given number is",self.number**3)
        print("***************************************************")

    def squareroot(self):
        print("The squareroot of a given number is",self.number**0.5)        

        
a=calculater(" ")
a.square()
a.cube()
a.squareroot()
