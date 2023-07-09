 
 

'''A = open('m.txt', 'r')
Lines = A.readlines()
line=A.readline()

count = 0

for line in Lines:
	count = count + 1
	print("L{}: {}".format(count, line.strip()))'''


 
 
def fre(m,letter):
    A = open('m.txt', 'r')
    Lines = A.read()
    Line=A.readline()
    return Line.count(letter)
print(fre('m.txt','y'))

#text="Python is object oriented"
 
dict={}
x = open('m.txt', 'r')
Lines = x.read()
Line=x.readline()

for x in 'm.text':
    if (x in 'm.txt'):
        dict[x]+=1
    else:
        dict[x]=1
print(dict ,'\n')


