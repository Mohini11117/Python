'''L={"M",'Family'}
a=open('.txt','w')
a.writelines(L)
a.close()
L=open('.txt','r')'''


L = ["Python is object oriented\n", "Python is easy to learn\n", "Python code is Readable\n"]

 

A = open('myfile.txt', 'r')
Lines = A.readlines()
line=A.readline()

count = 0

for line in Lines:
	count = count + 1
	print("L{}: {}".format(count, line.strip()))

