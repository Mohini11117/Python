text=input("Enter a text")
if("make a lot of money" in text):
    spam=True
elif("buy now"in text):
    spam=True
else:
    spam=False
if(spam):
    print("this is spam")
else:
    print("this is not spam")
print("*********************************************************")
name=input("enter a char  name: ")
if(len(name)==10):
    print(" given character have lenth 10")
else:
    print("given char not have lenght 10")
print("*********************************************************")
friendlist=["yogi","saurabh","bhakti","apeksha"]
friend=input("enter my friend name")
if(friend in  friendlist):
    print("she/he is there always with mi")
else:
    print("he/she is not my friend")

