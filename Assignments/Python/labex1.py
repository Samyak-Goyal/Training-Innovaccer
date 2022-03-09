
##1
#num=int(input('Enter the number: '))

#if(num%7 ==0 ):
#   print(f"{num} is divisible by 7")
#else :
#   print(f"{num} is not divisible by 7")    


##2
#name = input("Enter the name: ")

#salary = float(input("Enter the salary: "))

#print(f"Name\t\tMonthly Salary\n****\t\t**************\n{name.upper()}\t\t%.2f"%(salary))


##3
#myno=int(input("Enter Your No")) 
#result1=myno % 5 
#result2=myno % 8 
#if (result1==0 and result2==0): # 40 
#    print("%d is Divisible By Both 5 And 8" %myno) 
#elif (result1!=0 and result2==0): 
#    print("%d is Divisible by 8 But Not by 5" %myno) 
#elif (result1==0 and result2!=0): 
#    print("%d is Divisible by 5 But Not by 8" %myno) 
#elif (result1!=0 and result2!=0): 
#    print("%d is Not Divisible by 5 And 8" %myno) 
#print("Program Ended") 


##4
#while(True):

#    name = input("Enter the name: ").title().strip()
#    while(len(name) ==0):
#            name =input("Name cannot be blank, enter the name again: ").title().strip()
#    salary = float(input("Enter the salary: "))
#    while(salary< 30000):
#        print("Salary Cannot be less than 30k")
#        salary = float(input("Enter the salary again: "))
#    email=input("Enter Email: ")
#    while(not email.endswith('@innovaccer.com')):
#        email=input("Enter valid Email: ")

#    print(f"Name\t\tMonthly Salary\t\tEmail\n****\t\t**************\t\t*****\n{name}\t\t%.2f\t\t{email}"%(salary))
    
#    con=input("Continue?y/n: ")

#    if(con=='n' or con=='N'):
#        print("Program Ended")
#        break


##5
#for x in range(10,1,-2):
#    print(x)

##6
#num=int(input("Enter the number: "))

#for x in range(1,11):
#    print(f"{num} X {x}= {num*x}")
        

##7
#num=int(input("Enter any number: "))
#sum=0
#for x in range(1,num//2+1):
#    if(num%x==0):
#        sum+=x 

#if(sum==num):
#    print(f"{num} is a perfect number")        
#else:
#    print(f"{num} is not a perfect number")        


##8
#mystr="It is raining outside"
#words=mystr.split()
#print(len(words))


##9 
#ip=input("Enter the IP address: ")
#octats=ip.split(".")
#for x in octats:
#    print(x)


##10
#name="Innovaccer Analytics"
#short=name[0:3]  name[3] will be same
#print(short) #will print 'Inn'


#11
#name="Innovaccer Analytics"
#short=name[2:6] #will print 'nova'
#print(short)


##12
#name="Innovaccer Analytics"
#short=name[5::] #will print 'accer Analytics'
#print(short)


##13
#mystr="pqrs"
#print(mystr[::-1])  #reverse the string 


##14
#mystr=input("Enter the string: ")
#temp=mystr[::-1]
#if(mystr==temp):
#    print("The given string is a palindrome")
#else:
#    print("The given string is not a palindrome")


##15
#num=input("Enter the number: ")
#print(num[::-1])


##16
#circuitid="Lon/Lon/LE-123456"

#temp1=circuitid.split("/")

#temp2=temp1[2]

#temp2=temp2[:2]+"XXX"+temp2[2:6]+"XXX"
#print(temp2)


##17
#name=input("Enter the Employee Name: ").strip().title()
#mobno=input("Enter the mobile number: ").strip()
#while(True):
#    if(len(mobno)==10 and mobno.isdigit()):
#       break
#    else:
#        mobno=input("Enter Valid number: ").strip()
#print(mobno,name)












