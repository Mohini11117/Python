Num1=int(input("Enter a First number: "))
Num2=int(input("Enter a Second number: "))
Num3=int(input("Enter a Third number: "))
Num4=int(input("Enter a Fourth number: "))
if((Num1>Num2)&(Num1>Num3)&(Num1>Num4)):
    print("num1 is greter")
elif((Num2>Num3)&(Num2>Num4)):
    print("num2 is greter")
elif(Num3>Num4):
    print("num3 is greter")
else:
    print("num4 is greter ",Num4)
    print("*********************************************")
sub1=int(input("Enter a Marks of student: "))
sub2=int(input("Enter a Marks of student: "))
sub3=int(input("Enter a Marks of student: "))
if(sub1<33 | sub2<33 | sub3<33):
    print("Student is fail ")
elif((sub1+sub2+sub3)/3<40):
    print("your fail")


else:
    print("student is pass")








