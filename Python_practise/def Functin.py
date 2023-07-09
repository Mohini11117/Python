'''def cube(list):
    list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    for i in list:
        k=i*i*i
        print(k)
cube(list)'''
    
'''def pascal_triangle(n):
   rows = [1]
   column = [0]
   for x in range(max(n,0)):
      print(rows)
      rows=[l+r for l,r in zip(rows+column, rows+column)]
   return n>=1
pascal_triangle(5) '''
'''#program 8
#roll no2
def pascal_triangle(n):
   row = [1]
   column = [0]
   for x in range(max(n,0)):
      print(row)
      row=[l+r for l,r in zip(row+column, column+row)]
   return n>=1
pascal_triangle(5) 
'''
#sorting= lambda
'''T=[8,9,6,4,5,3,2,1]
print("Original list of tuples:")
print('T= ',T)
T.sort(key = lambda x: x[1])
print("\nSorting the List of Tuples:")
prin(T)'''
Student = [('Bhakti',17), ('Mohini',2), ('Apeksha',3), ('Saurabh',34),('Anuja',30)]

Student.sort(key=lambda s:s[1])

print(Student)
