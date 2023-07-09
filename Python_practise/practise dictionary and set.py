Dict={"khana":"eat","sona":"sleep","ghar":"home"}
a=input("Enter the hindi word\n")
print("The meaning of entered niumber is:" ,Dict.get(a))#it not throw an error if the key is
#not present in
#a=int(input("enter a number"))
#=int(input("enter a number"))
#c=int(input("enter a number"))
#d=int(input("enter a number"))
#e=int(input("enter a number"))
#g=int(input("enter a number"))
#f=int(input("enter a number"))
#k=int(input("enter a number"))
#l=int(input("enter a number"))###
#s={a,b,c,d,e,f,g,k,l}
#print(s)
b={18,"18"}
print(b)
s=set()
s.add(20)
s.add(20.3)
print(s)
print(len(s))
s={}
print(type(s))
favLang={}
a=input("Enter fav lang of shubham\n :")
b=input("Enter fav lang of raj\n :")
c=input("Enter fav lang of anju\n :")
d=input("Enter fav lang of raj\n :")
favLang['shubham']=a
favLang['raj']=b
favLang['anju']=c
favLang['raj']=d
print(favLang)



