class programmer:
    company ="Microsoft"
    def __init__(self,name,department):
        self.name=input("enter a name of Employee is: " )
        self.department=input("Enter a department name is: ")
        print("employee info is created!!!")
        print("**************************************")
    def details(self):
            print("name of employee",self.name)
            print("Department name",self.department)
m=programmer(" "," ")
n=programmer(" "," ")
n.details()
m.details()
    
        
        
