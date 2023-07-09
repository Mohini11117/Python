num1=int(input("enter a number"))
num2=int(input("enter a number"))
num3=int(input("enter a number"))
def maximum(num1,num2,num3):
    if(num1>num2&num1>num3):
        return num1
       # print(num1,"is greter") 
    elif(num2>num3):
        return num2
       # print(num1,"is greter")
    else:
        return num3
        #(num3,"is greter")

m= maximum(num1,num2,num3)
print("The value of maximum is: ",m)
print("*******************************************")
cel=int(input("enter a celcius temp"))
def far(cel):
    return(cel*(9/5))+32
print("converted value",far(cel))
print("*******************************************")

def sumN(n):
    if n==1:
        return 1
    else:
        return sumN(n-1)+n
print(sumN(4))
        


