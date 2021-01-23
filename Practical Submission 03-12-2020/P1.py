#Create a user defined function to find max of three number.
def num(a,b,c):
    if(a>=b and a>=c):
        print("Highest number: ",a)
    elif(b>=a and b>=c):
        print("Highest number: ",b)
    elif(c>=a and c>=b):
        print("Highest number: ",c)

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
num(a,b,c)