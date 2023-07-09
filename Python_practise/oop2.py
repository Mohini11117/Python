class Employee:
    company="Google"
    def Info(self):
         print("name of employee is:",self.name)
         print(self.company)

CompanyInfo=Employee()
CompanyInfo.name="Mohini"
CompanyInfo.company
Employee.company="Microsoft"
CompanyInfo.Info()
