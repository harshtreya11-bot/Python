str1="This is a string"
str2='Harsh Atreya'
str3="""This is a \n string"""
str4="""This is a \t string"""
print(str1)
print(str2)
print(str3)
print(str4)
str5="Harsh"
str6="Atreya"
Final_str=str5+str6
print(Final_str)
str7="Harsh"
str8="Atreya"
Final_str2=str7+str8
print(Final_str2)
str9="Komal"
len1=len(str9)
print(len1)
str10='my name is Harsh Atreya'
print(str10.capitalize())
print(str10.replace("a","e"))
print(str10.find("Harsh"))
print(str10.count("Harsh Atreya"))
name= input("Entre your name :")
print("length of Your name is:",len(name))

#Conditional Statement
age=21
if(age>=18):
    print("can Vote")

light='green'    
if(light=="red"):
    print("stop")
elif(light=='green'): 
    print("go")
elif(light=="yellow"):
    print("look")    

#Practice Based on Conditional Statement    

print("Find Grade of Student:")
marks=int(input("Entre your marks"))
if(marks>=90):
    print("You got Grade A")
elif(marks<90 and marks>=80):
    print("You got Grade B")  
elif(marks<80 and marks>=70):
    print("You got Grade c")  
elif(marks<70 and marks>=40):
    print("You got Grade D")  
else:
    print('You Got Failed')
    
                    
       