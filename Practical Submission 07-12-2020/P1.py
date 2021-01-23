#Using user defined function, Create calculator for different mathematical operations.
def add1(n1,n2):
    return n1 + n2
def sub2(n1,n2):
    return n1 - n2
def multi3(n1,n2):
    return n1 * n2
def div4(n1,n2):
    return n1 / n2
print("Operation: add, sub, multi, div:  ")
op=input("Select any one operation: ")
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
add=add1(num1,num2)
sub=sub2(num1,num2)
multi=multi3(num1,num2)
div=div4(num1,num2)
if op==add:
    print("Answer: ",add)
elif op==sub:
    print("Answer: ",sub)
elif op==multi:
    print("Answer: ",multi)
elif op==div:
    print("Answer: ",div)