# #Loops are used to repeat instructions 
# #First we learn while loop
# #while T :
# #    print("Hello")
#  #this print Hello infinitely because there 
#  #is no stopage
# count = 1000
# while count >= 1 :
#        print("Hello Harsh", count)
#        count -= 1
# #for print value from upward to downward   
# # never create infinite loop in code


# #Practice of While loop
# # print number from 1 to 100
# i=1
# while i <= 100:
#      print(i)
#      i+=1 

# #print number from 100 to 1
# i=100
# while i>= 1:
#       print(i)
#       i-=1

# #print the multiplication table of a number n
# n = int(input("Entre the number for table :" ))   
# i=1
# while i <=50 :
#     print(i*n)
#     i+=1

# #print following number in list
# nums = [1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx < len(nums):
#       print(nums[idx])
#       idx += 1

# #found the element from the list
# Super_hero = ("Iron Man","Captain America","Hulk","Thor")
# x = str(input("Entre the name of super hero : "))

# i=0
# while i<len(Super_hero):
#       if(Super_hero[i] == x):
#             print("Found The super Hero",x ,"at index",i) 
#       else:
#             print("finding")
#       i +=1     
# else:
#           print("not Found")

# #Break & Continue
# # Break: used to terminate the loop when encountered
# x= str(input("Entre staff name :"))
# y= str(input("Entre staff name :"))
# z= str(input("Entre staff name :"))
# w= str(input("Entre staff name :"))
# b= str(input("Entre staff name :"))
# Office_Staff =[x,y,z,w,b]
# print(Office_Staff)

# a = str(input("Entre staff name for search :"))

# i=0
# while i<len(Office_Staff):
#       if(Office_Staff[i]==a):
#             print("Found the Office Staff",a, "at the number",i)
#             break
#       else:
#             print("Not found the office staff")      
#       i +=1     
# #Continue for Skip a step or command
nums = ["Harsh Atreya","Aditya Sharma","Gunjan","Kumkum"]
n = int(input("Number of list element you want to remove"))
i=0
while i< len(nums) :
      if(i== n) :
            i += 1
            continue #Skip
      print(nums[i])    
      i += 1  

#for loops 
#for loops are used for sequential traversal,
list = [1,2,3]
for num in list:25
print(num)

