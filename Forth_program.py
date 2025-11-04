#dictionarry aree use to store data valuse in key:value pairs
#they are unordered, muteble and don't allow dublcate key
#let's take an example
Student ={
    "Name" : "Harsh Atreya",
    "Class" : "2nd Year", 
    "subject" : ["OOPs","DSA","MEFA","AEM"],
    "Marks" : ("60","55","44","50")
}
print(Student)

info = {
    "first_Name" : "Gunjan ", #string,
    "Last_Name" : "Saxena",
    "Subject" : ["Python","Java","C++"], #List
    "Topic" : ("Dist","Set"), #tuples
    "age" : 19, #integer
    "Marks" : 23.5 , #float value
}

print(info)
#to print specific data types of of dictionary
print(info["first_Name"])
print(info["Topic"])
print(info["age"])

#dictionary is mutable so we can edit its  data type
info["height"] = 5.10 ,
info["Full name"] = "Gunjan Saxena",
print(info)

#we can also create nnull dictionary
null_dict = {}
#we can also add value in null dictionary like
null_dict["name"] = "Sahil Samariya"

print(null_dict)
#we use to nested dictionary to required info from nested dictionary example
Student_k_section ={
    "Name" : "Bharat Saini",
    "Subjects" : {
        "AEM" : 12,
        "MEFA": 15,
        "OOPs": 40,
    }
}
print(Student_k_section)
print(Student_k_section["Subjects"]["MEFA"])

#Methos in Dictionary 
print(Student_k_section.keys())#to return all values
print(list(Student_k_section.keys())) #All keys in list value
print(len(list(Student_k_section.keys()))) #length of total keys
print(Student_k_section.items()) #return all the value of in the form of tuples
print(Student_k_section.get("Name")) #Using get method in direction we get none value if we entre the wrong key not the error

#mydict.update is also a method to insert a vale in old dictionary through new dictionary
#Example:-
New_Dict ={
    "Name": "Harsh Atreya"
}
Student_k_section.update(New_Dict)
print(Student_k_section)

#Set In Python
#Set is a collection of unordered Items
#Each element in Set is unique and Imutable
#Example
College ={1,2,2,2,2,2,3,4,7,8,"Harsh","Gunjan",} #Set ignoore repeat values
print(College)
print(type(College))
print(len(College))

#method of Set 
College.add(5)#to add a value or element in th Set
College.add(6)
College.add(12)
print(College)
College.remove(2) #To remove the element from set

#Method for Clear the Set
Child = {2,5,6,7,8,"Lokesh Aloria","Abhay Rathore"}
print(Child)
print(len(Child))
Child.clear()
print(len(Child))

#POP to remove rendom value from the Set 
College.pop
print(College)

#Union and Intersection in Set
College_Student = {"Harsh Atreya","Guunjan Saxena","Shalini Joshi","Aditya Sharma"}
Class_Student = {"Harsh Atreya","Krishna Sharma","Bharat Saini"}
print(College_Student.union(Class_Student)) #It print All Value of Both Sets
print(College_Student.intersection(Class_Student)) #it print only common values of both Set


#Practice of Dictionary
Word_Meaning = {
    "table" : ["A piece of Furniture","List of Fact and Figure"],
    "cat" : "a small animal"
}

# From the list of the Subject Find the number of 
#Class room are requird for the subject
Subjects_of_K_section  = {"python","Java","C++","python","Javascript"}
Subjects_of_C_section = {"Java","pyhton","Java","C++","C"}
print(Subjects_of_K_section)
print(Subjects_of_C_section)
print(Subjects_of_K_section.union(Subjects_of_C_section))
print("Number of Required Class :",len(Subjects_of_K_section.union(Subjects_of_C_section)))



#Print the marks of 3 subject of a student direct input from user
#the deictionary is Complete empty befor
marks = {}
x = int(input("Entre physicus marks : "))
marks.update({"physicus marks": x})

y = int(input("Entre Maths marks : "))
marks.update({"Maths marks": y})

z = int(input("Entre English marks : "))
marks.update({"English marks": z})
a=x+y+z
marks.update({"total marks of all subject " : a })
b= a/300 * 100
marks.update({"Total Percentage " : b})

print(marks)

