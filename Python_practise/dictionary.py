MyDict={"Name":{"Mohini":"player"},"Friend":"apeksha","clg":"ICOER",1:2}
print(MyDict["Name"])
print(MyDict["Name"]["Mohini"])
#Methods
print(MyDict.keys())#print keys 
print(type(MyDict.keys()))
print(list(MyDict.keys()))
print(MyDict.values())#print the values of keys
print(MyDict.items())#print the values and keys
print(MyDict)    #we can update dictionary
c={"granda'm":"lovely","Divya":"friend"}
MyDict.update(c)
print(MyDict)
print(MyDict.get("Name"))#print value of key associated with the key
print(MyDict["Name"])
print(MyDict.get("Name2"))#.get method print non if key is not present
print(MyDict["Name2"])#this method print error












