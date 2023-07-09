#program5
#roll 2
s={1,2,3,5,6,7,9}
s1={1,3,5,10}
list=[1,4,6,7,8]
touple=(1,2,3,6,7)
print("""for
1)set
2)list
3)touple""")
choice1=int(input("Enter a choice1"))
print("""To find
1)min
2)max
3)len
4)common element
5)exit""")
if (choice1==1):
    choice=int(input("Enter a choice"))
    if(choice==1):
        print(min(s))
    elif (choice==2):
        print(max(s))
    elif (choice==3):
        print(len(s))
    elif(s &s1):
        print("common elements are",s&s1)
    else:
        exit
elif(choice1==2):
    choice=int(input("Enter a choice"))
    if(choice==1):
        print(min(list))
    elif (choice==2):
        print(max(list))
    elif (choice==3):
        print(len(list))
    else:
        exit
elif(choice1==3):
    choice=int(input("Enter a choice"))
    if(choice==1):
        print(min(touple))
    elif (choice==2):
        print(max(touple))
    elif (choice==3):
        print(len(touple))
    else:
        exit
     
     
    
