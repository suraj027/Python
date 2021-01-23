#Write a program in Python to swap two numbers creating user defined function.
def swap(n1,n2,):
 sw=n1
 n1=n2 
 n2=sw
num1=float(input("Enter first number to swap: "))
num2=float(input("Enter second number to swap: "))
sp=swap(num1,num2)
print("After swap, first number: ",sp)
print("After swap. second number: ",sp)