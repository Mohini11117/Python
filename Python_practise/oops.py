#a=int(input("enter a number"))
#b=int(input("enter a number"))
class Number:
    def sum(self):
        return self.a+self.b
num=Number()
num.a=int(input("enter a number"))

num.b=int(input("enter a number"))

s=num.a+num.b
print(s)
class RailwayForm:
    formType="RailwayForm"
    def printData(self):
         print("name of Applicant:",self.name)
         print("name of Train is:",self.train)
         print("Time of Train  is:",self.time)

         
myApplication=RailwayForm()
myApplication.name=input("enter a Name of candidate: ")
myApplication.train=input("enter a name of train: ")
myApplication.time="5:00am"
myApplication.printData()
     
