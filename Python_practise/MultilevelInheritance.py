class person:
    country="India"
    def TakeBreath(self):
        print("i am  breathing...")
class Employee(person):
    company="Honda"
    def TakeBreath(self):
        print("i am luckily breathing..")
    def Getsalery(self):
        print("salery is :",self.salery)
class Programmer(Employee):
    company="fiver"
   # def TakeBreath(self):
   #     print("i am luckily breathing ++!!!!..")
    def Getsalery(self):
        print("No salery to programmer")
p=person()
e=Employee()
pr=Programmer()
pr.TakeBreath()

     
     
    
