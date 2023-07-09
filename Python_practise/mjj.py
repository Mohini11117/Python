s={1,2,3,45,6}
s1={1,5,4}
for
print("""To find
1)min
2)max
3)len
4)common element
5)exit""")
choice=int(input("Enter a choice"))
print(s)
if (choice==1):
    print(min(s))
elif (choice==2):
    print(max(s))
elif (choice==3):
    print(len(s))
elif(s &s1):
    print("common elements are",s&s1)
else:
    exit
