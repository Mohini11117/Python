f=open('C:/Users/Mohini11/OneDrive/Documents/sample.txt','r')
data=f.read(2)
print(data)
f.close()
f=open('C:/Users/Mohini11/OneDrive/Documents/sample.txt','r')
f.write("i am appending")
f.close()
