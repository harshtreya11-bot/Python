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
print(list(Student_k_section.items)) #return all the value of in the form of tuples


