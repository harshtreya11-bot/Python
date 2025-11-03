#lists in Python(Array of Python)
marks = [95.4,45.4,98.5,85.4,69.8,25.8,26.9]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
marks[6]=input("Marks of Sixth Student")
print(marks)
#List Sliceing means Call the List member From any point 
print(marks[1:5])
print(marks[-1:-5])
#append=add value in list which can be add in last of the list
marks1=[4,2,3,1]
last_value=input("Last value:")
marks1.append(last_value)
print(marks1)
#sorting in python is a method to arrange  list in asending order if it is integer,float or string
#marks1.sort()
#marks1.sort()
#print(marks1)
marks1.reverse()
#reverse the list
print(marks1)
#marks.remove for remove the element
marks1.remove(2)
print(marks1)


#Tuples in Python
#Tuples are also built in Database to store Collection
tup =(1,2,3,4,5,)
print(type(tup))

#for print tuple we should use , after the value 
t1=(2,)
print(type(t1))
#sliceing in Tuple
print(tup [1:4])
#index in tuple for fund value through address
t5=input(tup.index(5))
print(tup.index(5))
print(tup)
#count in Tuple for count the repetation of numbers
print(tup.count(2))





