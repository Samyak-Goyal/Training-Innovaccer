
from random import randint 

print("Welcome to Incare DashBoard")

min=int(input("Please enter min number : "))
max=int(input("Please enter max number : "))

if(min> max):
    print("Invalid Input")

else:
    random = randint(min,max)
    print("Random Number based on input is: ",random)    