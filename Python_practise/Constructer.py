class Employee:
    company="Google"
    def __init__(self,name,salery,subunit):
        self.name=input("Enter a name")
        self.salery=input("Enter salery")
        self.subunit=input("Enter a subunit")

        print("Employee is created!!")
    def getDetails(self):
        print("The name of Employee is: ",self.name)
        print("Salery   of Employee is: ",self.salery)
        print("Subunit  of Employee is: ",self.subunit)

m=Employee("M",10,"it")
m.getDetails()

