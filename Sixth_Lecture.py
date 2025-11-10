#Recursion is use in python for doesn't rpeat rhe Code
#function Defination
def Calu_Sum(a,b):
    return a+b

sum= Calu_Sum(2,5)
print(sum)

sum= Calu_Sum(3,4)
print(sum)

#A function which calculate the average of 5 number
def avg(a,b,e):
    return (a+b+e)/3

d = int(input("Entre the frst value : "))
g = int(input("Entre the second value : "))
f = int(input("Entr the third value : "))

done = avg(d,g,f)
print(done)

#types of function
#Built in function
#User define function

#WAP to print length of a list (list is parameter)
Colleges = ["Arya","JECRC","Poornima","JEC"]
Section_in_Arya = ["A","B","C","D","E","F","G"]

def print_len(list):
    print(len(list))

print_len(Colleges)    
print_len(Section_in_Arya)

#for items in list 
#Use loop

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(Colleges)        
#WAP to print the factorial of n
#def Factorial(n):
   # i=1
   # j=1
  #  while i<=n:
   #     j*=i
 #       j+=1


#WAP to convert USD to indian doller
def Converter(USD):
    INR = USD*83
    print(USD,"USD =",INR,"INR")

USD_value=int(input("The Doller you want to convert  :"))
Converter(USD_value)   

#WAF to find that the value is even or odd
def Even_odd(OddEven_val):
    if OddEven_val%2 == 0:
        print("Number is even")

    else :
        print("number is Odd")  

v = int(input("Entre the value for findd even or Odd :"))  
Even_odd(v)    

    
