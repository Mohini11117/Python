class Employee:
    company="Visa"
    eCode=120
class Freelancer:
    company="fiverr"
    level=0
    
    def upgradeLevel(self):
        self.level=self.level+1
class programmer(Employee,Freelancer):
    name="Mi"
p=programmer()
p.upgradeLevel()
print(p.level)
