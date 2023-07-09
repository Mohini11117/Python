num1=int(input("enter a two number :" ))
num2=int(input("enter a two number :"))

def sum(num1,num2):
    return num1+num2
s=sum(num1,num2)    
print("sum of given number",s)
print("***************************************************")

def greet(name):
    print("good Day, ",name)
greet("mohini")
print("***************************************************")

n=int(input("enter a value: "))
product=1
for i in range (n):
    product=product*(i+1)
print(product)
print("***************************************************")

n=int(input("enter a value: "))
def factorial(n):
    product=1
    for i in range(n):
        product=product*(i+1)
    return product
print(factorial(n))
